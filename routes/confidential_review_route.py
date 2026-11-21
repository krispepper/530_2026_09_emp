from flask import Blueprint, request
from confidential_review import confidential_review


submit_confidential_bp = Blueprint('submit_confidential', __name__)

@submit_confidential_bp.route("/submitConfidential", methods = ['POST'])
def submitReview_page():
    
    reviewID = request.form['reviewID']
    employeeID = request.form['employeeID']
    feedback = request.form['feedback']
    status = request.form['status']

    if reviewID is None: 
        message = models.confidential_review.submit_confidential(reviewID, employeeID, feedback, status)

    else:
        message = models.confidential_review.submit_inProgress(reviewID, feedback, status)

    return message

@submit_confidential_bp.route("/deleteInProgress", methods = ['POST'])
def delete_in_Progress_page():

    reviewID = request.form['reviewID']
    message = confidential_review.delete(reviewID, None)
    return message

from flask import Blueprint, request
from confidential_review import confidential_review


submit_confidential_bp = Blueprint('submit_confidential', __name__)

@submit_confidential_bp.route("/submitConfidential", methods = ['POST'])
def submitReview_page():
    
    reviewID = request.form['reviewID']
    employeeID = request.form['employeeID']
    feedback = request.form['feedback']
    status = request.form['status']

    if reviewID is None: 
        message = models.confidential_review.submit_confidential(reviewID, employeeID, feedback, status)

    else:
        message = models.confidential_review.submit_inProgress(reviewID, feedback, status)

    return message

@submit_confidential_bp.route("/deleteInProgress", methods = ['POST'])
def delete_in_Progress_page():

    reviewID = request.form['reviewID']
    message = confidential_review.delete(reviewID, None)
    return message

