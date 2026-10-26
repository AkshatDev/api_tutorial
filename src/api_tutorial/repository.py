"""Save and look up stations in the database."""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .exceptions import DuplicateSlugError
from .models import Station


class StationRepository:
    """Repository layer between the DB table 'stations' and the app.

    Args:
        session: A database connection session.


    """

    def __init__(self, session: Session) -> None:
        """Initialize the repo with a connection to the DB (session)."""
        self.session = session

    def add(self, station: Station) -> None:
        """Add a station, sending it to the database straight away so that errors appear here.

        It is only saved permanently when the caller commits.

        Args:
            station: A new station (row) for the table stations.

        Raises:
            DuplicateSlugError: If duplicate slug (Attribute of stations table) is added to the stations table. slug is unique (see models.py)
        """
        try:
            self.session.add(station)
            self.session.flush()
        except IntegrityError as error:
            raise DuplicateSlugError(station.slug) from error

    def get_by_slug(self, slug: str) -> Station | None:
        """Get a station by slug.

        Args:
            slug: Attribute for the stations table, station's URL-friendly identifier, e.g. ``beat-fm``.

        Returns:
            The matching station, or None if no station has that slug.

        """
        statement = select(Station).where(Station.slug == slug)
        return self.session.scalars(statement).one_or_none()
