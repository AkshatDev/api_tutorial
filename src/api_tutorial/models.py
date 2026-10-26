"""Module for table schemas for this application."""

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Parent class for all database models."""


class Station(Base):
    """Database schema class for ``stations`` table."""

    __tablename__ = "stations"

    id: Mapped[int] = mapped_column(primary_key=True)
    """Auto incremented unique key."""

    slug: Mapped[str] = mapped_column(String(30), unique=True)
    """URL-friendly identifier for station name, e.g. ``beat-fm``. Unique, at most 30 characters."""

    name: Mapped[str]
    """Station name in english."""

    genre: Mapped[str]
    """Music or content genre e.g. "pop", "rock", "news". """
