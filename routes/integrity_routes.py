# Purpose: Integrity check page - shows whether each submitted review is unchanged (controller only, no SQL).
# Author: Maaz Majeed
from flask import Blueprint, render_template
from models.review_integrity import ReviewIntegrity, TAMPERED, DELETED

integrity_bp = Blueprint('integrity', __name__)


# Integrity check page: runs the check and lists every submitted review's status
@integrity_bp.route('/integrity')
def integrity_check():
    results = ReviewIntegrity.check_all()
    problems = [r for r in results if r['status'] in (TAMPERED, DELETED)]
    return render_template('integrity.html', results=results, problems=problems)
