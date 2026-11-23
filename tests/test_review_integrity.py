# Purpose: Unit tests for detecting changes to submitted reviews (ReviewIntegrity).
# Author: Maaz Majeed
from datetime import date
from models.review_integrity import ReviewIntegrity, VERIFIED, TAMPERED, DELETED

REVIEW = {'reviewID': 1, 'reviewerID': 10002, 'employeeID': 10003,
          'feedback': 'Great teamwork', 'submissionDate': date(2026, 11, 21)}


# Fake database: in-memory review tables and fingerprint table, no MySQL needed
class FakeDatabase:
    def __init__(self, open_reviews=(), confidential_reviews=(), fingerprints=None):
        self.tables = {'SubmitOpenReview': [dict(r) for r in open_reviews],
                       'SubmitConfidentialReview': [dict(r) for r in confidential_reviews]}
        self.fingerprints = dict(fingerprints or {})

    def query(self, sql, params=None):
        if 'FROM ReviewFingerprints' in sql:
            return [{'reviewType': t, 'reviewID': i, 'contentHash': h} for (t, i), h in self.fingerprints.items()]
        table = 'SubmitOpenReview' if 'SubmitOpenReview' in sql else 'SubmitConfidentialReview'
        return [dict(r) for r in self.tables[table]]

    def execute(self, sql, params=None):
        review_type, review_id, content_hash = params
        self.fingerprints[(review_type, review_id)] = content_hash
        return 1


def use_fake(monkeypatch, fake):
    monkeypatch.setattr('models.review_integrity.Database.get_instance', lambda: fake)


def test_same_review_gives_same_hash():
    assert ReviewIntegrity.compute_hash(REVIEW) == ReviewIntegrity.compute_hash(dict(REVIEW))


def test_changed_feedback_gives_different_hash():
    changed = dict(REVIEW, feedback='Poor teamwork')
    assert ReviewIntegrity.compute_hash(changed) != ReviewIntegrity.compute_hash(REVIEW)


def test_new_review_is_fingerprinted_and_verified(monkeypatch):
    fake = FakeDatabase(open_reviews=[REVIEW])
    use_fake(monkeypatch, fake)
    results = ReviewIntegrity.check_all()
    assert ('Open', 1) in fake.fingerprints
    assert [r['status'] for r in results] == [VERIFIED]


def test_edited_review_is_flagged_as_tampered(monkeypatch):
    original_hash = ReviewIntegrity.compute_hash(REVIEW)
    edited = dict(REVIEW, feedback='Poor teamwork')
    use_fake(monkeypatch, FakeDatabase(confidential_reviews=[edited],
                                       fingerprints={('Confidential', 1): original_hash}))
    results = ReviewIntegrity.check_all()
    assert results[0]['status'] == TAMPERED


def test_deleted_review_is_flagged(monkeypatch):
    use_fake(monkeypatch, FakeDatabase(fingerprints={('Open', 1): ReviewIntegrity.compute_hash(REVIEW)}))
    results = ReviewIntegrity.check_all()
    assert results == [{'reviewType': 'Open', 'reviewID': 1, 'employeeID': None,
                        'submissionDate': None, 'status': DELETED}]
