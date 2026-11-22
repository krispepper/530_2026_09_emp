from flask import Blueprint, request
from models.confidential_review import confidential_review


submit_confidential_bp = Blueprint('submit_confidential', __name__)

@submit_confidential_bp.route("/submitConfidential", methods = ['POST'])
def submitReview_page():
    
    reviewID = request.form['reviewID']
    reviewerID = request.form['reviewerID']
    employeeID = request.form['employeeID']
    feedback = request.form['feedback']
    status = request.form['status']

    periodID = request.form['periodID']

    if reviewID == "":
        reviewID = None

    message = confidential_review.submit_confidential(reviewID, reviewerID, employeeID, feedback, "Submitted")

    return message



# @submit_confidential_bp.route("/deleteInProgress", methods = ['POST'])
# def delete_in_Progress_page():

#     reviewID = request.form['reviewID']
#     message = confidential_review.delete(reviewID, None)
#     return message
