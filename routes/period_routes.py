# Purpose: Review period pages - list periods and add a new one (controller only, no SQL here).
# Author: Maaz Majeed.
from datetime import date
from flask import Blueprint, render_template, request
from models.review_period import ReviewPeriod
from queries import get_employees

period_bp = Blueprint('periods', __name__)


def _parse_date(value):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def _render(message=None, error=None, status=200):
    return render_template('periods.html', periods=ReviewPeriod.get_all(),
                           employees=get_employees(), message=message, error=error), status


@period_bp.route('/periods')
def list_periods():
    return _render()


@period_bp.route('/periods', methods=['POST'])
def add_period():
    name = request.form.get('periodName', '')
    try:
        ReviewPeriod.add(
            name,
            _parse_date(request.form.get('startDate')),
            _parse_date(request.form.get('deadlineDate')),
            request.form.get('isConfidential') == 'on',
            request.form.get('createdBy'),
        )
    except ValueError as e:
        return _render(error=str(e), status=400)
    return _render(message='Review period created')
