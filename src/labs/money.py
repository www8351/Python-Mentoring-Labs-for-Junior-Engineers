"""Money exercises: market checkout and ad-campaign costing.

The originals reused variables and applied VAT inconsistently. These return
typed, immutable results and apply VAT exactly once.
"""

from __future__ import annotations

from dataclasses import dataclass

VAT_RATE = 0.18
"""Default value-added-tax rate."""


@dataclass(frozen=True)
class MarketResult:
    """Outcome of a market checkout."""

    subtotal: float
    vat: float
    total: float
    change: float


@dataclass(frozen=True)
class CampaignResult:
    """Outcome of an ad-campaign cost estimate."""

    daily_rate: float
    days: int
    platforms: int
    total: float


def market_total(
    items: list[tuple[str, float, int]],
    paid: float,
    vat_rate: float = VAT_RATE,
) -> MarketResult:
    """Total an ``(name, unit_price, quantity)`` basket and return the change.

    VAT is applied once to the subtotal. ``change`` is ``paid - total`` and may
    be negative when the customer underpays.
    """
    if vat_rate < 0:
        raise ValueError("vat_rate must be >= 0")
    if any(price < 0 or qty < 0 for _, price, qty in items):
        raise ValueError("prices and quantities must be >= 0")
    subtotal = sum(price * qty for _, price, qty in items)
    vat = subtotal * vat_rate
    total = subtotal + vat
    return MarketResult(subtotal=subtotal, vat=vat, total=total, change=paid - total)


def campaign_cost(daily_rate: float, days: int, platforms: int = 1) -> CampaignResult:
    """Cost of running an ad campaign across ``platforms`` for ``days`` days."""
    if daily_rate < 0:
        raise ValueError("daily_rate must be >= 0")
    if days < 0:
        raise ValueError("days must be >= 0")
    if platforms < 1:
        raise ValueError("platforms must be >= 1")
    total = daily_rate * days * platforms
    return CampaignResult(daily_rate=daily_rate, days=days, platforms=platforms, total=total)
