"""The main entry point for the application to start a FastAPI application."""

import uvicorn
from fastapi import FastAPI

from .schemas import Health


def create_app() -> FastAPI:
    """Create a FastAPI application."""
    app = FastAPI()

    @app.get("/health")
    async def health() -> Health:
        """Report that the service is running."""
        return Health(status="ok")

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app)
