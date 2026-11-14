# Purpose: ReviewPeriod model - validates and reads/writes the ReviewPeriods table.
# Author: Maaz Majeed.
from datetime import date
from db import Database


class ReviewPeriod:
    def __init__(self, period_id, period_name, start_date, deadline_date, is_confidential, created_by):
        self.period_id = period_id
        self.period_name = period_name
        self.start_date = start_date
        self.deadline_date = deadline_date
        self.is_confidential = bool(is_confidential)
        self.created_by = created_by

    @property
    def is_closed(self):
        return self.deadline_date < date.today()

    @staticmethod
    def _from_row(row):
        return ReviewPeriod(row['periodID'], row['periodName'], row['startDate'],
                            row['deadlineDate'], row['isConfidential'], row['createdBy'])

    @staticmethod
    def get_all():
        rows = Database.get_instance().query(
            'SELECT * FROM ReviewPeriods ORDER BY startDate DESC')
        return [ReviewPeriod._from_row(r) for r in rows]

    @staticmethod
    def validate(name, start_date, deadline_date, existing_names, created_by):
        """Returns an error message, or None if the period is valid."""
        if not created_by:
            return 'Please select who is creating this period'
        if not name or not name.strip():
            return 'Please enter a period name'
        if start_date is None or deadline_date is None:
            return 'Please enter a start date and a deadline'
        if deadline_date <= start_date:
            return 'Deadline must be after the start date'
        if name.strip().lower() in (n.lower() for n in existing_names):
            return 'A review period with this name already exists'
        return None

    @staticmethod
    def add(name, start_date, deadline_date, is_confidential, created_by):
        """Saves a new period. Raises ValueError with a user-facing message if invalid."""
        existing = [p.period_name for p in ReviewPeriod.get_all()]
        error = ReviewPeriod.validate(name, start_date, deadline_date, existing, created_by)
        if error:
            raise ValueError(error)
        Database.get_instance().execute(
            'INSERT INTO ReviewPeriods (periodName, startDate, deadlineDate, isConfidential, createdBy) '
            'VALUES (%s, %s, %s, %s, %s)',
            (name.strip(), start_date, deadline_date, is_confidential, created_by))
