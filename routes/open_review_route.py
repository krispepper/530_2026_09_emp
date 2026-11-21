# Author: Branson Jamanram
# Description: The python flask code for submitting open reviews
# Checks all the cases where a review can be submitted

from flask import Blueprint, render_template, request
from models.open_review import open_review


submit_open_bp = Blueprint('submit_open', __name__)

@submit_open_bp.route("/submitOpen", methods = ['POST'])
def submitReview_page():
    
    reviewID = request.form['reviewID']
    employeeID = request.form['employeeID']
    feedback = request.form['feedback']
    status = request.form['status']

    if reviewID is None: 
        message = models.open_review.submit_open(reviewID, employeeID, feedback, status)

    else:
        message = models.open_review.submit_inProgress(reviewID, feedback, status)

    return message

@submit_open_bp.route("/deleteInProgress", methods = ['POST'])
def delete_in_Progress_page():

    reviewID = request.form['reviewID']
    message = open_review.delete(reviewID, None)
    return message

