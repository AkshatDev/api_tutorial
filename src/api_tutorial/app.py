"""The main entry point for the application to start a FastAPI application."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from .log_config import configure_logging
from .schemas import Health


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Run start-up and shutdown code for the app.

    Logging is configured here rather than in ``create_app()``: the server applies its own logging setup after importing the app, which would overwrite ours.
    """
    configure_logging()
    yield


def create_app() -> FastAPI:
    """Create a FastAPI application."""
    app = FastAPI(lifespan=lifespan)

    @app.get("/health")
    async def health() -> Health:
        """Report that the service is running."""
        return Health(status="ok")

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app)
