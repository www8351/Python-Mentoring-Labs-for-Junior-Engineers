<div align="center">

# 🎓 Python Mentoring Labs for Junior Engineers

**A guided, test-driven path from buggy beginner scripts to clean, typed, production-style Python.**

Each lab is a small, self-contained exercise — a pure typed function you can read, run, test, break, and fix. Curated and mentored from the perspective of an AI & DevOps Architect, so you don't just learn *syntax*, you learn the *habits* that make engineers trusted with real systems.

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

- [Who this is for](#-who-this-is-for)
- [Curriculum index — what each lab teaches](#-curriculum-index--what-each-lab-teaches)
- [Cross-cutting engineering concepts](#-cross-cutting-engineering-concepts)
- [Install & run](#-install--run)
- [How to use this repository for self-study](#-how-to-use-this-repository-for-self-study)
- [From buggy scripts to clean code (a teaching artifact)](#-from-buggy-scripts-to-clean-code-a-teaching-artifact)
- [Develop](#-develop)

---

## 🎯 Who this is for

This repo is for **junior engineers and self-learners** who can already write a
few lines of Python and now want to learn how *professionals* structure code.

You'll practice the move that separates a beginner from an engineer: turning a
quick interactive script into a **pure function** that is easy to read, type,
test, and reason about — then exposing it through a clean command-line
interface.

Every example here started life as a beginner `input()` script, several with
real bugs. They've been rebuilt as typed functions with full test coverage, so
you can study *both* the finished, professional version **and** the mistake it
replaced.

By working through the labs you will learn to:

- Separate **logic** from **input/output**.
- Write **pure, deterministic functions** that are trivial to test.
- Use **type hints** and a strict type checker to catch bugs before runtime.
- Cover behavior — including edge cases — with **unit tests**.
- Handle invalid input deliberately instead of letting it crash later.

---

## 🗂 Curriculum index — what each lab teaches

Each lab is one CLI command backed by one or more functions in `src/labs/`.
Work through them top to bottom: the order is deliberately **simplest →
trickiest**, so you build confidence before the labs with the gnarly bugs.

| # | Lab / Command | Source module | Core concepts | Why it matters |
|---|---------------|---------------|---------------|----------------|
| 1 | `multiplication-table` | [`arithmetic.py`](src/labs/arithmetic.py) | list comprehensions, tuples, `range`, **returning data vs. printing it** | The foundational habit: build a value, return it, print it *somewhere else*. |
| 2 | `digits` | [`arithmetic.py`](src/labs/arithmetic.py) | integer math (`%`, `//`), loops, building a list, slice reversal `[::-1]`, edge cases (`0`, negatives) | Decomposing a number by hand teaches how data is represented, plus disciplined edge-case thinking. |
| 3 | `palindrome` | [`text.py`](src/labs/text.py) | string normalization, filtering comprehension, `str.isalnum`, slice reversal, two-pointer intuition | "Clean your input first" is a lesson you'll reuse for the rest of your career. |
| 4 | `fib` | [`arithmetic.py`](src/labs/arithmetic.py) | iteration vs. recursion, **tuple-unpacking swap** (`a, b = b, a + b`), base cases, off-by-one / index bugs | The classic interview problem — and a real lesson in how a missed base case becomes a crash. |
| 5 | `market` | [`money.py`](src/labs/money.py) | **frozen `@dataclass` results**, immutability, input validation, getting money/VAT math right *once* | Your first taste of **domain modeling**: name your outputs instead of juggling loose variables. |
| 6 | `campaign` | [`money.py`](src/labs/money.py) | parameters & defaults, validation guards (`ValueError`), keeping calculation free of I/O | Small, total, well-guarded functions are the building blocks of reliable systems. |
| 7 | `lottery` | [`lottery.py`](src/labs/lottery.py) | **dependency injection** of `random.Random` for determinism, `random.sample` for unique draws, **set intersection** for scoring | How do you test *randomness*? You inject the randomness — a pattern that scales to databases, clocks, and network calls. |

---

## 🧱 Cross-cutting engineering concepts

Beyond the per-lab topics, the repository as a whole is a worked example of the
habits a tech lead looks for:

- **Pure functions** — same input, same output, no hidden side effects. The
  random labs accept an injected RNG so they stay deterministic.
- **Separation of concerns** — all logic lives in `src/labs/*`; the CLI in
  [`src/labs/cli.py`](src/labs/cli.py) only parses arguments and prints. Logic
  never knows it's behind a terminal.
- **Type hints + `mypy --strict`** — the type checker is a free second reviewer
  that runs on every commit.
- **Unit tests with `pytest`** — one test module per lab in [`tests/`](tests/),
  so behavior is pinned down and refactoring is safe.
- **Input validation** — functions raise clear `ValueError`s on bad input
  instead of failing mysteriously later.
- **Linting & formatting** — `ruff` keeps style consistent so reviews focus on
  substance.
- **Continuous integration** — [`.github/workflows/ci.yml`](.github/workflows/ci.yml)
  runs lint + format + type-check + tests on every push.

---

## 📦 Install & run

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management.

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

Run any command with `--help` to see its options.

---

## 🧭 How to use this repository for self-study

This is a guided lab, not a finished product to admire. Treat it the way you'd
treat a mentor sitting next to you: be curious, run things, and **break them on
purpose** to understand why they're built the way they are.

### 1. Follow the path in order

Work the labs **1 → 7** as listed in the [curriculum index](#-curriculum-index--what-each-lab-teaches).
They escalate from "warm-up" to "this one had a real, subtle bug," so each lab
prepares you for the next.

### 2. The mentoring loop — repeat for every lab

For each lab, do all five steps before moving on. This is the loop professional
engineers run on real code, scaled down:

1. **Read the function and its docstring.** Read the code in `src/labs/`
   *before* running it. Predict the output in your head.
2. **Run it through the CLI** and check your prediction:
   ```bash
   uv run labs fib 10
   ```
3. **Read its test** in `tests/`. Notice *what* is asserted — especially the
   edge cases (zero, negatives, empty input, underpayment).
4. **Break it on purpose.** Change a line in the source (an off-by-one, a wrong
   operator) and run the tests. Watch them fail — *a failing test is the system
   working*:
   ```bash
   uv run pytest -k fibonacci
   ```
5. **Re-derive the fix** and get back to green. Then `git checkout` the file to
   restore it and move on.

### 3. Push yourself — make it your own

Once the loop feels comfortable, stretch:

- Add a **recursive** `fibonacci` next to the iterative one and write a test
  proving they agree for `n = 0..20`.
- Add a brand-new lab: a function in `src/labs/`, a CLI subcommand in
  `cli.py`, and a matching test module. **Tests and types are part of "done."**
- Tighten validation somewhere and add the test that proves the new guard fires.
- Run the full quality gate (below) until it's all green before you'd call any
  change finished.

### 4. A note from your mentor 🧑‍🏫

The tests, the type hints, and the CI pipeline are not busywork — they are how
engineers earn the trust to ship code other people depend on. Junior developers
see them as hoops; senior engineers see them as the **safety net that lets them
move fast without fear**. Internalize that mindset early and you'll grow faster
than the syntax alone would ever take you.

Write code you can explain. Test the behavior you care about. Make the next
person to read it — often future-you — thank you.

---

## 🧪 From buggy scripts to clean code (a teaching artifact)

These labs are refactors of real beginner scripts, several of which contained
genuine bugs. Studying the *before* is half the lesson — each fix maps directly
to a concept above:

| Before ❌ | After ✅ | The lesson |
|----------|---------|-----------|
| `while "True":` menus blocking on `input()` | non-interactive Typer subcommands | separate logic from I/O |
| Lottery assigned `list.append(...)` → `None`, breaking every later comparison | real unique draw + clean set-based scoring | know what your expressions *return* |
| Fibonacci read `seq[i-1]` when `i < 2` (index error) | base cases handled first | always handle the boundary cases |
| Market/campaign reused variables, applied VAT inconsistently | typed `@dataclass` results, VAT applied once | model your domain; name your outputs |
| No functions, no tests | pure functions + full `pytest` suite | make behavior testable and pinned |

---

## 🧰 Develop

The full local quality gate — run it before considering any change done:

```bash
uv run ruff check .
uv run ruff format .
uv run mypy src
uv run pytest
```

CI runs lint + format + mypy + tests on every push, so green locally means green
on the pull request.

---

<div align="center">

*Built as a mentoring resource. Read it, run it, break it, fix it — then teach the next person.*

</div>
