# Purpose: Detects changes to submitted reviews. Each submitted review gets a SHA-256
# fingerprint; later checks compare the review's current content to that fingerprint.
# Author: Maaz Majeed
import hashlib
from models.db import Database

# Review type -> table that holds it
REVIEW_TABLES = {
    'Open': 'SubmitOpenReview',
    'Confidential': 'SubmitConfidentialReview',
}

VERIFIED = 'Verified'
TAMPERED = 'Tampered'
DELETED = 'Deleted'


class ReviewIntegrity:

    @staticmethod
    def compute_hash(review):
        """Fingerprint the parts of a review that must never change after submission.

        review: dict with reviewerID, employeeID, feedback, submissionDate.
        Returns: str, 64-character SHA-256 hex digest.
        """
        content = '|'.join(str(review[k]) for k in ('reviewerID', 'employeeID', 'feedback', 'submissionDate'))
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    @staticmethod
    def _submitted_reviews():
        """Returns: list of dicts for every submitted review, with a reviewType key added."""
        db = Database.get_instance()
        reviews = []
        for review_type, table in REVIEW_TABLES.items():
            rows = db.query(f'SELECT reviewID, reviewerID, employeeID, feedback, submissionDate '
                            f'FROM {table} WHERE status = %s', ('Submitted',))
            for row in rows:
                row['reviewType'] = review_type
                reviews.append(row)
        return reviews

    @staticmethod
    def _fingerprints():
        """Returns: dict {(reviewType, reviewID): contentHash} of every stored fingerprint."""
        rows = Database.get_instance().query(
            'SELECT reviewType, reviewID, contentHash FROM ReviewFingerprints')
        return {(r['reviewType'], r['reviewID']): r['contentHash'] for r in rows}

    @staticmethod
    def record_new():
        """Store a fingerprint for every submitted review that doesn't have one yet.

        Returns: int, how many new fingerprints were stored.
        """
        known = ReviewIntegrity._fingerprints()
        count = 0
        for review in ReviewIntegrity._submitted_reviews():
            key = (review['reviewType'], review['reviewID'])
            if key not in known:
                Database.get_instance().execute(
                    'INSERT INTO ReviewFingerprints (reviewType, reviewID, contentHash) VALUES (%s, %s, %s)',
                    (key[0], key[1], ReviewIntegrity.compute_hash(review)))
                count += 1
        return count

    @staticmethod
    def check_all():
        """Compare every submitted review to its fingerprint.

        New submitted reviews are fingerprinted first, so they show as Verified.
        Returns: list of dicts (reviewType, reviewID, employeeID, submissionDate, status),
        status is Verified, Tampered (content changed) or Deleted (review removed).
        """
        ReviewIntegrity.record_new()
        known = ReviewIntegrity._fingerprints()
        results = []
        seen = set()
        for review in ReviewIntegrity._submitted_reviews():
            key = (review['reviewType'], review['reviewID'])
            seen.add(key)
            status = VERIFIED if known.get(key) == ReviewIntegrity.compute_hash(review) else TAMPERED
            results.append({'reviewType': key[0], 'reviewID': key[1], 'employeeID': review['employeeID'],
                            'submissionDate': review['submissionDate'], 'status': status})
        # A fingerprint with no matching submitted review means it was deleted or un-submitted
        for key in known:
            if key not in seen:
                results.append({'reviewType': key[0], 'reviewID': key[1], 'employeeID': None,
                                'submissionDate': None, 'status': DELETED})
        return results
