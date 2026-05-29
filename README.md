<div align="center">

# 🧪 labs

**A pile of beginner Python scripts, rebuilt as pure, tested functions with one clean CLI.**

Every exercise is now a typed function you can import, test, and call from the terminal.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/packaged%20with-uv-DE5FE9?logo=astral&logoColor=white)
![Ruff](https://img.shields.io/badge/lint-ruff-D7FF64?logo=ruff&logoColor=black)
![mypy](https://img.shields.io/badge/types-mypy%20strict-2A6DB2)
![pytest](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)
![Typer](https://img.shields.io/badge/CLI-Typer-009688)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

---

## 📖 Table of contents

- [What changed](#-what-changed)
- [Upgrade order](#-upgrade-order)
- [Install & run](#-install--run)
- [The labs](#-the-labs)
- [Develop](#-develop)

---

## 💡 What changed

The originals were interactive `input()` scripts, several with real bugs. Now:

| Before ❌ | After ✅ |
|----------|---------|
| `while "True":` menus blocking on `input()` | non-interactive Typer subcommands |
| Lottery assigned `list.append(...)` → `None`, all comparisons broken | real unique draw + clean scoring |
| Fibonacci read `seq[i-1]` when `i < 2` (index error) | base cases handled first |
| Market/campaign reused vars, applied VAT wrong | typed results, VAT applied once |
| No functions, no tests | pure functions + full `pytest` |

---

## 🗺 Upgrade order

Rebuilt simplest → buggiest, so each step was easy to verify before the hard ones:

| # | Command | From | Fix |
|---|---------|------|-----|
| 1 | `multiplication-table` | Multiplication_Table.py | already clean — made it a function |
| 2 | `digits` | Math.py | digit extraction, validated input |
| 3 | `palindrome` | DNS.py | case/space-insensitive |
| 4 | `fib` | Fibo_Check+Fix.py, Lab_2.py | **fixed `i < 2` index error** |
| 5 | `market` | Marketing.py, Lab_2 §4 | **fixed pricing, VAT once** |
| 6 | `campaign` | Campiagn.py | **fixed change/sign logic** |
| 7 | `lottery` | Lottery.py | **fixed `None`-assignment bug** |

> Skipped: the cube game (now lives in the `ossys` repo) and the pure-demo
> `List.py` / DNS dictionary snippets.

---

## 📦 Install & run

```bash
uv sync --dev

uv run labs multiplication-table 5
uv run labs digits 1234
uv run labs palindrome racecar
uv run labs fib 10
uv run labs market tomato:3:2 bread:5:1 --paid 20
uv run labs campaign 100 10 --platforms 2
uv run labs lottery --seed 42 --ticket 1,5,9,12,30,37
```

---

## 🧱 The labs

| Module | Functions |
|--------|-----------|
| `arithmetic.py` | `multiplication_table`, `extract_digits`, `fibonacci`, `is_valid_fibonacci` |
| `text.py` | `is_palindrome` |
| `money.py` | `market_total`, `campaign_cost` |
| `lottery.py` | `draw`, `score` |

All are pure and deterministic (the random ones accept an injected `rng`), so they test cleanly.

---

## 🧪 Develop

```bash
uv run ruff check .
uv run ruff format .
uv run mypy src
uv run pytest
```

CI runs lint + format + mypy + tests on every push.
