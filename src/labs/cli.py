"""Typer CLI exposing every lab as a non-interactive subcommand."""

from __future__ import annotations

import random

import typer
from rich.console import Console

from labs import arithmetic, lottery, money, text

app = typer.Typer(help="Small Python labs as CLI commands.", no_args_is_help=True)
console = Console()


@app.command("multiplication-table")
def multiplication_table(n: int, up_to: int = 10) -> None:
    """Print the multiplication table for ``n`` up to ``up_to``."""
    for a, b, product in arithmetic.multiplication_table(n, up_to):
        console.print(f"{a} x {b} = {product}")


@app.command()
def digits(number: int) -> None:
    """Print the base-10 digits of ``number``."""
    console.print(arithmetic.extract_digits(number))


@app.command()
def fib(n: int) -> None:
    """Print the ``n``-th Fibonacci number."""
    console.print(arithmetic.fibonacci(n))


@app.command()
def palindrome(value: str) -> None:
    """Report whether ``value`` is a palindrome."""
    console.print(text.is_palindrome(value))


@app.command()
def market(
    items: list[str],
    paid: float = typer.Option(..., "--paid", help="Amount the customer paid."),
) -> None:
    """Total a basket of ``name:price:qty`` items and show the change."""
    basket: list[tuple[str, float, int]] = []
    for token in items:
        try:
            name, price, qty = token.split(":")
            basket.append((name, float(price), int(qty)))
        except ValueError as exc:
            raise typer.BadParameter(f"expected name:price:qty, got {token!r}") from exc
    result = money.market_total(basket, paid)
    console.print(
        f"subtotal={result.subtotal:.2f} vat={result.vat:.2f} "
        f"total={result.total:.2f} change={result.change:.2f}"
    )


@app.command()
def campaign(daily_rate: float, days: int, platforms: int = 1) -> None:
    """Estimate the cost of an ad campaign."""
    result = money.campaign_cost(daily_rate, days, platforms)
    console.print(f"total={result.total:.2f}")


@app.command("lottery")
def lotto(
    ticket: str = typer.Option(..., "--ticket", help="Comma-separated numbers."),
    seed: int | None = typer.Option(None, "--seed", help="Seed for a reproducible draw."),
) -> None:
    """Draw winning numbers and score ``--ticket`` against them."""
    rng = random.Random(seed) if seed is not None else random.Random()
    winning = lottery.draw(rng=rng)
    numbers = [int(part) for part in ticket.split(",")]
    matches = lottery.score(numbers, winning)
    console.print(f"winning={winning} matches={matches}")


if __name__ == "__main__":
    app()
