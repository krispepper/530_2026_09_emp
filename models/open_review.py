# Author: Branson Jamanram
# Description: Uses 2 functions that allow employees to
# Submit an open review in full, and checks for duplicates

from datetime import date
from models.db import Database

class open_review:


    # Submit an open review in full
    @staticmethod
    def submit_open(reviewID, reviewerID, employeeID, periodID, feedback, status):
        # If there is no reviewID then you can submit an open review

        if reviewID is None:

            if open_review.duplicate_review(reviewerID, employeeID, periodID) == True:

                return "Duplicate reviews are not allowed"

            else:

                Database.get_instance().execute(
                'INSERT INTO SubmitOpenReview (reviewerID, employeeID, periodID, feedback, submissionDate, status) '
                'VALUES (%s, %s, %s, %s, %s, %s)',
                (reviewerID, employeeID, periodID, feedback, date.today(), "Submitted"))
                
                return "Submitted"

        else:

            return "Something went wrong"


    @staticmethod
    def duplicate_review(reviewerID, employeeID, periodID):
            query = Database.get_instance().query(
            'SELECT reviewID '
            'FROM SubmitOpenReview '
            'WHERE reviewerID = %s '
            'AND employeeID = %s '
            'AND periodID = %s '
            'AND status = %s ',
            (reviewerID, employeeID, periodID, 'Submitted'))

            # Cannot return a string otherwise the databse doesnt know if its
            # A duplicate or not
            if len(query) > 0:
                return True
            
            else:
                return False




# ** These methods have not be implemented yet **#


    # @staticmethod
    # def delete(reviewID, status):
    #     if reviewID is not None and status == "In Progress":
    #         Database.get_instance().execute(
    #         'DELETE FROM SubmitOpenReview '
    #         'WHERE reviewID = %s '
    #         'AND status = %s ',
    #         (reviewID, "In Progress"))

    #         return "The review has been deleted"



    # # If a review is in progress, you are allowed to update the draft
    # @staticmethod
    # def submit_inProgress(reviewID, feedback, status):
    #     if reviewID is not None and status == "In Progress":
    #         Database.get_instance().execute(
    #             'UPDATE SubmitOpenReview '
    #             'SET feedback = %s, submissionDate = %s, status = %s ' 
    #             'WHERE reviewID = %s ',
    #             (feedback, date.today(), "Submitted", reviewID))
            
    #         return "Review is now submitted"
        
    #     else:
    #         return "You cannot submit this review"

