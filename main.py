"""Main entrypoint."""

from src.api import api

if __name__ == "__main__":
    # this is when you run it as script
    import uvicorn

    uvicorn.run(app=api)
