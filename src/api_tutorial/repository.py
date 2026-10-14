from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .exceptions import DuplicateSlugError
from .models import Station


class StationRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, station: Station) -> None:
        try:
            self.session.add(station)
            self.session.flush()
        except IntegrityError as error:
            raise DuplicateSlugError(station.slug) from error

    def get_by_slug(self, slug: str) -> Station | None:
        statement = select(Station).where(Station.slug == slug)
        return self.session.scalars(statement).one_or_none()
