# LEDGER

## ISSUES

```
Issue:  Phase 0 (management files) is committed locally and waits for owner review.
Action: Owner reviews CLAUDE.md, LEDGER.md and the .gitignore block. Phase 1 starts only on owner instruction.
Status: OPEN
```

```
Issue:  Phase 1, infra and tooling. uv.lock is stale (records typer>=0.12, ruff>=0.6, mypy>=1.11) and CI re-locks silently. pre-commit pins ruff v0.9.6 and mirrors-mypy v1.15.0. Dependabot uses the pip ecosystem and never updates uv.lock. Python 3.10 is end of life.
Action: requires-python >=3.11, raise floors (ruff>=0.17.0, typer>=0.27.3, mypy>=2.4.0, pre-commit>=4.6.2), add pytest-cov, uv lock. CI with UV_LOCKED=1, UV_PYTHON per matrix leg, matrix 3.11 to 3.14, build job with wheel smoke test, workflow_call reused by release.yml with tag/version check. Dependabot ecosystem uv. pre-commit local hooks via uv run. Hatch dynamic version, __main__.py, py.typed, --version flag, required future import. Fix the two broken README anchors only.
Status: OPEN
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
Action: Full README rewrite, English section then Hebrew section, 13 lab curriculum, dev commands identical to CI. CHANGELOG 0.2.0. Version 0.2.0 then uv lock. Tag is created by the owner after merge.
Status: OPEN
```

```
Issue:  Open Dependabot PRs #27, #39, #40, #41 become obsolete after phase 1 raises the same floors.
Action: Owner closes them after phase 1 merges. Executor does not close them.
Status: BLOCKED (owner)
```

## ACTIONS

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
