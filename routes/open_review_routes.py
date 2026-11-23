# Author: Branson Jamanram
# Description: The python flask code for submitting open reviews
# Checks all the cases where a review can be submitted

from flask import Blueprint, render_template, request, session
from models.open_review import open_review
from models.employee import (get_employees, get_employeesID)
from models.review_period import ReviewPeriod


submit_open_bp = Blueprint('submit_open', __name__)


@submit_open_bp.route("/submit-reviews")
def openReview_page():

    employees = get_employees()
    periods = ReviewPeriod.get_all()



    return render_template("submit_review.html", employees = employees, periods = periods)
    

@submit_open_bp.route("/submitOpen", methods = ['POST'])
def submitReview_page():
    
    reviewID = request.form['reviewID']
    reviewerID = session.get('reviewerID')
    employeeID = request.form['employeeID']
    periodID = request.form['periodID']
    feedback = request.form['feedback']
    status = request.form['status']


    if reviewID == "":
        reviewID = None

    message = open_review.submit_open(reviewID, reviewerID, employeeID, periodID, feedback, "Submitted")

    return message

