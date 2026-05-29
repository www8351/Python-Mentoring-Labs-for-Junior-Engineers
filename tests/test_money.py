"""Tests for labs.money."""

from __future__ import annotations

import pytest

from labs import money


def test_market_total_applies_vat_once() -> None:
    result = money.market_total([("tomato", 3.0, 2), ("bread", 5.0, 1)], paid=20.0, vat_rate=0.0)
    assert result.subtotal == 11.0
    assert result.vat == 0.0
    assert result.total == 11.0
    assert result.change == 9.0


def test_market_total_with_vat() -> None:
    result = money.market_total([("item", 100.0, 1)], paid=100.0, vat_rate=0.18)
    assert result.vat == pytest.approx(18.0)
    assert result.total == pytest.approx(118.0)
    assert result.change == pytest.approx(-18.0)


def test_market_total_rejects_negative_vat() -> None:
    with pytest.raises(ValueError, match="vat_rate"):
        money.market_total([], paid=0.0, vat_rate=-0.1)


def test_campaign_cost() -> None:
    result = money.campaign_cost(100.0, 10, platforms=2)
    assert result.total == pytest.approx(2000.0)


def test_campaign_cost_rejects_zero_platforms() -> None:
    with pytest.raises(ValueError, match="platforms"):
        money.campaign_cost(100.0, 10, platforms=0)
