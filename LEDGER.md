# LEDGER

## ISSUES

```
Issue:  Phase 1 (infra and tooling) is committed locally in 4010644, ee0a931, 672150d, 09c413c and waits for owner review.
Action: Owner reviews phase 1. Phase 2 starts only on owner instruction. Push is not authorized for phase 1 yet.
Status: OPEN
```

```
Issue:  The new CI has never run on GitHub. setup-uv is pinned to tag v10.3.0, found by web search and not confirmed against the action repository. UV_LOCKED, UV_PYTHON per matrix leg, the build job and the workflow_call reuse are verified only by local simulation.
Action: Confirm on the first CI run after the owner authorizes a push. If v10.3.0 does not resolve, pin the version the action repository lists as latest.
Status: BLOCKED (owner, needs push)
```

```
Issue:  uv 0.13 makes Python 3.15 its default stable Python. The CI matrix stays 3.11 to 3.14 per the FINAL Python decision.
Action: None by the executor. Extending the matrix to 3.15 needs a new owner decision.
Status: OPEN (owner)
```

```
Issue:  Phase 2, code quality and tests. money.py uses float with no rounding. cli.py has no tests and the lottery --ticket parse can raise a traceback. Several edge cases are untested.
Action: Decimal money with LineItem and ROUND_HALF_UP to cents. Annotated CLI options, Decimal parser that maps InvalidOperation to BadParameter, lottery ticket validation. tests/test_cli.py with CliRunner. Edge case tests. Google docstrings, ruff D and PT. Coverage threshold set to the measured value, floor 95.
Status: OPEN
```

```
Issue:  Phase 3, exercise framework. The seven labs ship only finished solutions.
Action: exercises/labs mirrors src/labs with NotImplementedError stubs. exercises/labNN_<name>/ holds README.md and a reconstructed before.py. Root conftest.py adds --target {solution,exercise} with a verified sys.path shim. Per test labNN markers. AST based parity test. CI runs exercise collect-only.
Status: OPEN
```

```
Issue:  Phase 4, new labs 08 errors.py (exception hierarchy, raise from, ExceptionGroup) and 09 files.py (pathlib, JSON, CSV).
Action: Per lab order: before.py, red tests, solution, stub, README, CLI command and test.
Status: OPEN
```

```
Issue:  Phase 5, new labs 10 inventory.py (class invariants, slots dataclass) and 11 grouping.py (Counter, defaultdict).
Action: Same per lab order as phase 4.
Status: OPEN
```

```
Issue:  Phase 6, new labs 12 audit_log.py (getLogger, caplog) and 13 concurrency.py (TaskGroup, asyncio.timeout, injected sleep).
Action: Same per lab order as phase 4. No pytest-asyncio. Module names never shadow the stdlib.
Status: OPEN
```

```
Issue:  Phase 7, docs and release. README is not bilingual, has grammar broken by dash removal, and claims full coverage without a tool. CHANGELOG links point to the wrong repository.
Action: Full README rewrite, English section then Hebrew section, 13 lab curriculum, dev commands identical to CI. CHANGELOG 0.2.0. Version 0.2.0 in src/labs/__init__.py (uv.lock no longer stores the project version). Tag is created by the owner after merge.
Status: OPEN
```

```
Issue:  Open Dependabot PRs #27, #39, #40, #41 become obsolete after phase 1 raises the same floors.
Action: Owner closes them after phase 1 merges. Executor does not close them.
Status: BLOCKED (owner)
```

## ACTIONS

```
Issue:  2026-10-18. Phase 1, infra and tooling. Owner approved phase 0 and instructed to continue.
Action: 4010644 requires-python >=3.11, floors ruff>=0.17.0 typer>=0.27.3 mypy>=2.4.0 pre-commit>=4.6.2, pytest-cov added, uv.lock regenerated (it still recorded typer>=0.12, ruff>=0.6, mypy>=1.11). ee0a931 CI: UV_LOCKED=1, UV_PYTHON per job, matrix 3.11 to 3.14, setup-uv v3 to v10.3.0, build job with wheel smoke test; release.yml reuses ci.yml via workflow_call, checks tag against version, contents: write only on the release job; Dependabot ecosystem pip to uv. 672150d pre-commit: ruff and mypy as local hooks via uv run --frozen, uv lock --check hook, pre-commit-hooks v6.0.0 (rev confirmed by a successful hook install). 09c413c hatch dynamic version from src/labs/__init__.py, __main__.py, py.typed, --version option with a CliRunner test, required future import, two README anchors fixed. Tried: uv lock --check failed once after the dynamic version change because the lock still stored version 0.1.0; uv lock removed that line.
Status: DONE
```

```
Issue:  2026-10-18. Phase 0 review.
Action: Owner approved phase 0 and instructed phase 1 to run.
Status: DONE
```

```
Issue:  2026-10-18. Phase 0 commits existed only inside an ephemeral cloud container.
Action: Owner instructed a push without a pull request and without a merge. Branch ccr-a62d60e9-wykx88 pushed to origin. No PR opened, main untouched.
Status: DONE
```

```
Issue:  2026-10-18. Phase 0, management files.
Action: Created CLAUDE.md (protocol v3) and LEDGER.md. Added a *.md block with negations for README.md, CHANGELOG.md, /LEDGER.md and /CLAUDE.md to .gitignore so the owner's bootstrap script does not append its own block, plus coverage and editor ignores.
Status: DONE
```

```
Issue:  2026-10-18. Planning session, full repository audit.
Action: Found 23 passing tests, clean ruff, stale uv.lock, stale pre-commit pins, pip ecosystem Dependabot, float money, untested CLI, two broken README anchors, no exercises or before scripts. Owner answered the scoping questions and approved an 8 phase plan (phase 0 to phase 7).
Status: DONE
```

## DECISIONS

```
Issue:  Which tracks the roadmap covers. Source: owner answer in planning session 2026-10-18.
Action: Infra and tooling, code quality and tests, new labs. Not selected as a separate track: learning structure (the exercise model was decided by its own question below).
Status: FINAL
```

```
Issue:  How students get exercises versus solutions. Source: owner answer in planning session 2026-10-18.
Action: Separate exercises/ folder with starter code; solutions stay in src/labs. Rejected: separate solutions branch; solutions only.
Status: FINAL
```

```
Issue:  Which labs get the exercise model. Source: owner answer in planning session 2026-10-18.
Action: All labs, the existing seven and every new one. Rejected: new labs only.
Status: FINAL
```

```
Issue:  Topics for new labs. Source: owner answer in planning session 2026-10-18.
Action: Exceptions and files; classes and data structures; logging and asyncio. Not selected: generators and iterators.
Status: FINAL
```

```
Issue:  Supported Python versions. Source: owner answer in planning session 2026-10-18.
Action: Floor 3.11, CI matrix adds 3.14. Rejected: keep 3.10.
Status: FINAL
```

```
Issue:  Push policy at the end of each phase. Source: owner answer in planning session 2026-10-18.
Action: Local commits only. Push and pull requests only on explicit owner instruction. Rejected: push and draft PR after every phase.
Status: FINAL
```

```
Issue:  Management files in this repository. Source: owner answer in planning session 2026-10-18.
Action: Create CLAUDE.md and LEDGER.md and commit them to git. Rejected: local only; do not create.
Status: FINAL
```

```
Issue:  Exercise mechanism. Source: executor proposal inside the plan the owner approved on 2026-10-18, not an owner ruling.
Action: pytest option --target with a sys.path shim verified by labs.__file__, per test labNN markers, AST based stub parity test. Rejected: per test impl fixture (loses static typing in tests); separate copies of tests per lab.
Status: REVISIT
```

```
Issue:  Money arithmetic. Source: executor proposal inside the approved plan, not an owner ruling.
Action: decimal.Decimal built from strings, quantize to cents with ROUND_HALF_UP inside the domain function. Rejected: float with round(), which rounds half to even.
Status: REVISIT
```

```
Issue:  Single source for tool and package versions. Source: executor proposal inside the approved plan, not an owner ruling.
Action: Hatch dynamic version read from src/labs/__init__.py. pre-commit runs ruff and mypy as local hooks through uv run, so versions come from uv.lock only. Rejected: importlib.metadata version (fails when run uninstalled); pinned mirror hooks (drift from the lock).
Status: REVISIT
```

```
Issue:  Markdown files and the owner's bootstrap script, which appends *.md and !README.md to .gitignore when no exact *.md line exists. Source: executor proposal inside the approved plan, not an owner ruling.
Action: Keep an exact *.md line in .gitignore followed by negations for README.md, CHANGELOG.md, /LEDGER.md and /CLAUDE.md. Every new .md file needs its own negation or a README.md name. Check with git status --short --ignored before each commit.
Status: REVISIT
```
