from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create a FastAPI application."""

    app = FastAPI()

    @app.get("/health")
    async def health()->dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
