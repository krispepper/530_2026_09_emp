# Author: Branson Jamanram
# Description: Uses multiple functions that allow employees to
# Submit an open review in full, save a draft, check for duplicates, reviews cant be changed,
# and allows the review to be deleted

from datetime import date
from models.db import Database

class open_review:


    # Submit an open review in full
    @staticmethod
    def submit_open(reviewID, reviewerID, employeeID, feedback, status):
        # If there is no reviewID then you can submit an open review
        if reviewID is None:
            Database.get_instance().execute(
            'INSERT INTO SubmitOpenReview (reviewerID, employeeID, feedback, submissionDate, status) '
            'VALUES (%s, %s, %s, %s, %s)',
            (reviewerID, employeeID, feedback, date.today(), "Submitted"))
            
            return "Submitted"

    # If a review is in progress, you are allowed to update the draft
    @staticmethod
    def submit_inProgress(reviewID, feedback, status):
        if reviewID is not None and status == "In Progress":
            Database.get_instance().execute(
                'UPDATE SubmitOpenReview '
                'SET feedback = %s, submissionDate = %s, status = %s ' 
                'WHERE reviewID = %s ',
                (feedback, date.today(), "Submitted", reviewID))
            
            return "Review is now submitted"
        
    @staticmethod
    def duplicate_review(reviewID, employeeID, status):
        if reviewID is not None:
            Database.get_instance().query(
            'SELECT reviewID '
            'FROM SubmitOpenReview '
            'WHERE employeeID = %s '
            'AND status = %s '
            'AND reviewID != %s ',
            (employeeID, 'Submitted', reviewID))

            return "You can only submit a review for the employee once"
            
    # You are not allowed to change submitted reviews       
    @staticmethod
    def integrity(reviewID, status):
        if reviewID is not None and status == "Submitted":
            return "Submitted reviews cannot be edited"
        

    @staticmethod
    def delete(reviewID, status):
        if reviewID is not None and status == "In Progress":
            Database.get_instance().execute(
            'DELETE FROM SubmitOpenReview '
            'WHERE reviewID = %s '
            'AND status = %s ',
            (reviewID, "In Progress"))

            return "The review has been deleted"
