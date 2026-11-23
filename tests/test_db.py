# Purpose: Unit tests for the shared Database connection (Singleton).
# Author: Maaz Majeed
from models.db import Database


class FakeConnection:
    autocommit = False


def test_shared_connection_uses_autocommit(monkeypatch):
    monkeypatch.setattr('models.db.get_connection', lambda: FakeConnection())
    assert Database()._conn.autocommit is True


def test_get_instance_returns_same_object(monkeypatch):
    monkeypatch.setattr('models.db.get_connection', lambda: FakeConnection())
    monkeypatch.setattr(Database, '_instance', None)
    assert Database.get_instance() is Database.get_instance()
