# Contributing

Thanks for adding to the question bank. Each "pack" is a self-contained practice codebase with
deliberately planted bugs. The whole point is that **every test fails by default** and a candidate
has to find and fix the bugs. Keep that contract and new packs will fit right in.

## Where packs live

- `round-1/<codename>/` — a small, focused service (target ~35 minutes).
- `round-2/<codename>/` — a larger, multi-module microservice (target ~45 minutes).

Use a **codename** that reveals nothing about the domain (for example `halcyon`, `kestrel`). The
README tells the story; the folder name does not.

## Languages and layout

A pack keeps its **spec and tickets shared** and puts the code in a per-language subfolder, so one
problem can exist in several languages:

```text
<codename>/
  README.md    shared: welcome, repository map, product rules, how to run each language
  tickets/     shared: one .md per reported problem
  python/      codes.py ..., tests/ (pytest), conftest.py
  cpp/         *.hpp, tests.cpp, Makefile
  java/        *.java, Tests.java
```

There is **no SOLUTION.md** anywhere. The acceptance tests are the answer key: green means fixed.

### Test runners (dependency-free on purpose)

- **Python:** `cd python && pytest -q`. Tests are in `tests/test_acceptance.py`; a `conftest.py`
  puts the pack on the path.
- **C++:** `cd cpp && make test` (compiles `tests.cpp` with `g++ -std=c++17` and runs it). The
  runner prints `PASS`/`FAIL` per check and exits non-zero if any fail. Keep implementations
  header-only (`.hpp`) so `tests.cpp` just includes them.
- **Java:** `cd java && javac *.java && java Tests`. `Tests.java` has a `main` that runs checks and
  calls `System.exit(1)` on any failure.

## The rules (please keep these)

1. **Every test fails on the shipped code.** No passing "sanity" test. If a behaviour has no bug,
   it has no test.
2. **Each failing test isolates exactly one bug**, for one clear reason.
3. **Fixable to green.** After applying the intended fix, the whole suite must pass.
4. **No external dependencies, services, API keys, or network calls.** Standard library only
   (plus `pytest` for Python).
5. **Integer money.** If a pack handles money, use integer cents; no floats in the ledger.
6. **Realistic bugs.** Off-by-ones, idempotency gaps, boundary conditions, priority/ordering
   violations, missing validation. No syntax errors or obviously broken code.

## Adding a language port to an existing pack

Port the **same spec and the same planted bugs** into a new `cpp/` or `java/` folder next to
`python/`. The acceptance tests must cover the same behaviours and must all fail on the ported
(buggy) code, then all pass once the same fixes are applied. Do not change the shared `README.md`
or `tickets/` beyond adding the run commands for your language.

## README shape

Open with "Welcome to the team that ...", then include a **Run the tests** section (one block per
available language), a **Repository map**, and **Product rules already agreed** (the spec, as
bullets).

## Ticket shape (one file per problem, in `tickets/`)

```text
# <ID>: <short title>

## Report
<2-3 sentences: the symptom, when it happens, what is observed>

## Acceptance criteria
- <criterion>;
- <criterion>;
- add a test that <...>;

Do not redesign <X> as part of this ticket.
```

## Before you submit: verify the pack

For each language, the shipped pack must be all red, and all green once the intended fixes are
applied. A pack that cannot go from red to green is not ready. Keep the fixes out of the
repository.

## Opening a change

Create a branch, add your pack (or language port), and open a pull request. In the PR description
(not in the repo), list the codename, the round, the language(s), and the planted bugs, and
confirm the suite goes from red to green. Keep the solution out of the repository.
