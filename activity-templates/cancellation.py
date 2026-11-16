"""Cancellation operations for the booking application."""


def cancel_places(booked, quantity):
    """Cancel places and return the number remaining."""
    if quantity < 1:
        raise ValueError("Quantity must be at least one.")
    return booked - quantity
