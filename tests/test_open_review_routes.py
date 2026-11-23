# Purpose: Unit tests for submitting an open review without selecting a user first.
# Author: Maaz Majeed
from app import app

FORM = {'reviewID': '', 'employeeID': '10041', 'periodID': '2', 'feedback': 'Great work', 'status': 'In Progress'}


def test_submit_without_login_is_rejected(monkeypatch):
    saved = []
    monkeypatch.setattr('routes.open_review_routes.open_review.submit_open', lambda *args: saved.append(args))
    response = app.test_client().post('/submitOpen', data=FORM)
    assert response.status_code == 401
    assert saved == []


def test_submit_after_login_uses_session_reviewer(monkeypatch):
    saved = []
    monkeypatch.setattr('routes.open_review_routes.open_review.submit_open',
                        lambda *args: saved.append(args) or 'Submitted')
    client = app.test_client()
    with client.session_transaction() as session:
        session['reviewerID'] = '10001'
    response = client.post('/submitOpen', data=FORM)
    assert response.status_code == 200
    assert saved[0][1] == '10001'  # reviewerID comes from the session
