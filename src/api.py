"""API entry point."""

from fastapi import FastAPI, Request

api = FastAPI()


@api.post("/doctors")
async def available_doctors():
    """Get available doctors."""


@api.post("/doctor-availability")
async def doctor_availability(request: Request):
    """Get doctor availability schedule."""
    data = await request.json()
    print(data)


@api.post("/book")
async def book_appointment(request: Request):
    """Book appointment."""
    data = await request.json()
    print(data)
