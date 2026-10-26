"""Integration tests for ``StationRepository`` against real Postgres (each test is rolled back)."""

import pytest
from sqlalchemy.orm import Session

from api_tutorial import DuplicateSlugError, Station
from api_tutorial.repository import StationRepository


def test_saved_station_can_be_fetched(session: Session) -> None:
    repo = StationRepository(session)

    repo.add(Station(slug="beat-fm", name="Beat FM", genre="pop"))
    found = repo.get_by_slug("beat-fm")
    assert found is not None
    assert found.name == "Beat FM"


def test_unknown_slug_returns_none(session: Session) -> None:
    repo = StationRepository(session)
    assert repo.get_by_slug("does-not-exist") is None


def test_duplicate_slug_raises(session: Session) -> None:
    repo = StationRepository(session)

    repo.add(Station(slug="beat-fm", name="Beat FM", genre="pop"))

    with pytest.raises(DuplicateSlugError):
        repo.add(Station(slug="beat-fm", name="Duplicate Beat FM", genre="pop"))
