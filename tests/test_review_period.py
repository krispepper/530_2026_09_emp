# Purpose: Unit tests for the ReviewPeriod model (Sprint 1 review periods story).
# Author: Maaz Majeed
from datetime import date
import pytest
from models.review_period import ReviewPeriod

START = date(2026, 9, 1)
DEADLINE = date(2026, 12, 15)
CREATOR = 10001


def test_valid_period_has_no_error():
    assert ReviewPeriod.validate('Fall 2026', START, DEADLINE, [], CREATOR) is None


def test_deadline_before_start_is_rejected():
    error = ReviewPeriod.validate('Fall 2026', DEADLINE, START, [], CREATOR)
    assert error == 'Deadline must be after the start date'


def test_duplicate_name_is_rejected_ignoring_case():
    error = ReviewPeriod.validate('fall 2026', START, DEADLINE, ['Fall 2026'], CREATOR)
    assert error == 'A review period with this name already exists'


# Fake database so these tests never touch MySQL
class FakeDatabase:
    def __init__(self):
        self.saved = []

    def query(self, sql, params=None):
        return []

    def execute(self, sql, params=None):
        self.saved.append(params)
        return 1


def test_add_invalid_period_is_not_saved(monkeypatch):
    fake = FakeDatabase()
    monkeypatch.setattr('models.review_period.Database.get_instance', lambda: fake)
    with pytest.raises(ValueError, match='Deadline must be after the start date'):
        ReviewPeriod.add('Fall 2026', DEADLINE, START, False, CREATOR)
    assert fake.saved == []


def test_add_valid_period_is_saved_once(monkeypatch):
    fake = FakeDatabase()
    monkeypatch.setattr('models.review_period.Database.get_instance', lambda: fake)
    ReviewPeriod.add('  Fall 2026  ', START, DEADLINE, True, CREATOR)
    assert fake.saved == [('Fall 2026', START, DEADLINE, True, CREATOR)]
