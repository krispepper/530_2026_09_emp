from datetime import date
from models.db import Database

class confidential_review:


    # Submit an confidential review in full
    @staticmethod
    def submit_confidential(reviewID, reviewerID, employeeID, feedback, status):
        # If there is no reviewID then you can submit an confidnetial review
        if reviewID is None:

            if confidential_review.duplicate_review(employeeID) == True:

                return "Duplicate reviews are not allowed"

            else:

                Database.get_instance().execute(
                    'INSERT INTO SubmitConfidentialReview (reviewerID, employeeID, feedback, submissionDate, status) '
                    'VALUES (%s, %s, %s, %s, %s)',
                    (reviewerID, employeeID, feedback, date.today(), "Submitted"))
            
            return "Submitted"
        
        else:
            
            return "Something went wrong"


    @staticmethod
    def duplicate_review(employeeID):

        query = Database.get_instance().query(
            'SELECT reviewID '
            'FROM SubmitConfidentialReview '
            'WHERE employeeID = %s '
            'AND status = %s ',
            (employeeID, 'Submitted'))

        # Cannot return a string otherwise the databse doesnt know if its
        # A duplicate or not
        if len(query) > 0:
            return True
        
        else:
            return False


        return "Duplicate reviews are not allowed"
            



    @staticmethod
    def hide_name(employeeID):
            query = Database.get_instance().query(
            'SELECT reviewID, employeeID, feedback, submissionDate, status '
            'FROM SubmitConfidentialReview '
            'WHERE employeeID = %s '
            'AND status = %s ',
            (employeeID, 'Submitted'))

            return query




    # If a review is in progress, you are allowed to update the draft
    # @staticmethod
    # def submit_inProgress(reviewID, feedback, status):
    #     if reviewID is not None and status == "In Progress":
    #         Database.get_instance().execute(
    #             'UPDATE SubmitConfidentialReview '
    #             'SET feedback = %s, submissionDate = %s, status = %s ' 
    #             'WHERE reviewID = %s ',
    #             (feedback, date.today(), "Submitted", reviewID))
            
    #         return "Review is now submitted"
        

    # @staticmethod
    # def delete(reviewID, status):
    #     if reviewID is not None and status == "In Progress":
    #         Database.get_instance().execute(
    #         'DELETE FROM SubmitConfidentialReview '
    #         'WHERE reviewID = %s '
    #         'AND status = %s ',
    #         (reviewID, "In Progress"))

    #         return "The review has been deleted"
        

    # # You are not allowed to change submitted reviews       
    # @staticmethod
    # def integrity(reviewID, status):
    #     if reviewID is not None and status == "Submitted":
    #         return "Submitted reviews cannot be edited"
        
