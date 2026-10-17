# bloomberg-practice

Interview-grade practice for Bloomberg's AI-assisted codebase rounds. Each pack is an
**unfamiliar codebase** under a codename that reveals nothing about the domain, with
real, deliberately planted bugs and **no tests**.

That last part is the point. The real skill is not running a green suite someone handed
you. It is reading code you did not write, taking a vague bug report, forming a
hypothesis, **writing your own test to confirm it**, fixing the code, and keeping your
test green. So these packs ship the service and the reported symptom, and you bring the
tests.

- `round-1/` — a focused service: one stateful domain object with a clear lifecycle and a
  few planted bugs. Target ~35 minutes. A `CANDIDATE_BRIEF.md` tells you the system and
  the reported symptom; `PROJECT_MANAGER_NOTES.md` has the questions to ask.
- `round-2/` — a larger multi-module microservice with more surface area and a `tickets/`
  backlog of reported problems. Target ~45 minutes.

There are no solution files and no shipped tests. The code, the brief, and the tickets are
all you get, the same as walking into a real repository on your first day.

## Languages

Every pack is implemented three times, once per language, with the **same bugs**. Pick the
language you want to interview in.

```text
round-1/halcyon/                         round-2/harbor/
  README.md         scope                  README.md         scope + rules
  CANDIDATE_BRIEF.md                        SETUP.md
  PROJECT_MANAGER_NOTES.md                  tickets/
  SELF_REVIEW_AFTER.md                      python/  cpp/  java/
  SETUP.md
  python/  cpp/  java/
```

Each `python/` keeps a `conftest.py` so the tests you write import the module cleanly. The
C++ implementation is header-only, so you write a `test.cpp` that includes it. For Java you
write a small `Check.java` with a `main`. See each pack's `SETUP.md`.

## Setting up a working copy

`bin/bloomberg-practice` copies a pack into a working directory so you can edit it and add
your own tests without touching the shared packs. `create` makes a new folder named
`<codename>-<lang>` inside the directory you give it (the current directory by default).

```bash
bin/bloomberg-practice create marlin python ~/practice   # ~/practice/marlin-python/
bin/bloomberg-practice list --round 2
```

On Windows, use the bundled PowerShell launcher instead. Windows PowerShell 5.1 is built
in; PowerShell 7 (`pwsh`) is used automatically when available.

```bat
bin\bloomberg-practice.cmd create marlin python C:\practice   # C:\practice\marlin-python\
bin\bloomberg-practice.cmd list --round 2
```

Add `bin` to your `PATH` to run `bloomberg-practice` from anywhere. `create` copies the
pack's documents (round 1 briefs, or round 2 tickets), its `README.md`, and the code files
for only the language you choose, all into the new folder. The code sits at the project
root; there is no language subfolder. `SETUP.md` is not copied, because it describes the
repository layout rather than your generated project. It refuses a non-empty target folder
unless you pass `--force` (`-f`).

## Round 1 — one service, a few bugs (~35 min, Python / C++ / Java)

One stateful domain object with a lifecycle and invariants to protect. The brief gives you
the reported symptom; you find and confirm the bugs.

| Pack | Domain | What it is |
| --- | --- | --- |
| [halcyon](round-1/halcyon) | Order Lifecycle | Working orders placed, filled, and cancelled; open-quantity and over-fill invariants. |
| [marlin](round-1/marlin) | Inventory Reservations | TTL stock holds, commit versus release, expiry returns units automatically. |
| [zephyr](round-1/zephyr) | Subscription Entitlement | Trial, active, suspended, cancelled lifecycle with trial expiry. |
| [cobalt](round-1/cobalt) | Wallet Holds | Authorization holds, capture versus void, available equals balance minus holds. |
| [quasar](round-1/quasar) | Rate Limiter | Fixed-window per-key limiter with window reset and remaining quota. |
| [onyx](round-1/onyx) | Access Tokens | Short-lived tokens: issue, validate, refresh, revoke, with TTL expiry. |
| [pike](round-1/pike) | Approval Workflow | Documents go pending then approved, rejected, or withdrawn; terminal states. |
| [vesper](round-1/vesper) | Connection Pool | Fixed-capacity acquire, release, and close, with a capacity invariant. |
| [tundra](round-1/tundra) | LRU + TTL Cache | Capacity-bounded cache with per-entry TTL and least-recently-used eviction. |
| [lumen](round-1/lumen) | Job State Machine | Queued, running, done, failed, with retries and an attempt budget. |

## Round 2 — larger microservices (~45 min, Python / C++ / Java)

More modules, more surface area, a ticket backlog. Work ticket by ticket.

| Pack | Service | What it is |
| --- | --- | --- |
| [harbor](round-2/harbor) | Payments Service | Accounts, a double-entry ledger, holds, and idempotent transfers. |
| [meridian](round-2/meridian) | Calendar Service | Scored meeting requests scheduled in batches around protected events. |
| [cinder](round-2/cinder) | Market Data Service | A snapshot-plus-incremental quote cache with a subscription fan-out. |
| [drift](round-2/drift) | Fulfillment Service | A catalog, on-hand inventory, and reservations behind an availability view. |
| [aperture](round-2/aperture) | Job Orchestration | A ready queue, a registry, and a dispatcher with retries and dead-lettering. |
| [kestrel](round-2/kestrel) | Matching Engine | A single-symbol limit order book with price-time priority matching. |
| [basalt](round-2/basalt) | Risk Netting | Per-counterparty, per-symbol netting of signed trades. |
| [galena](round-2/galena) | Message Bus | Topic pub/sub with wildcard matching and isolated fan-out. |
| [saffron](round-2/saffron) | Session Service | A TTL session store with expiry, refresh, and cleanup. |
| [ridgeline](round-2/ridgeline) | Cache Tier | A capacity-bounded LRU cache. |

## How to practice

1. Pick a pack and a language, and start a timer (35 min for round 1, 45 min for round 2).
2. Read the pack (round 1: `CANDIDATE_BRIEF.md`; round 2: `README.md` and `tickets/`). Note
   the reported symptom, not a bug location.
3. Map the code. Form a hypothesis about what is actually wrong.
4. **Write a test that reproduces it** and watch it fail. That failing test is your proof
   the bug is real, and the thing you will turn green. See `SETUP.md` for how to run tests
   in each language.
5. Fix the narrowest layer. Keep every test you wrote green. Do not change behaviour the
   brief did not ask you to.
6. Narrate the whole time: the invariant each bug breaks, the state transitions, time and
   space complexity, whether the operation should be idempotent, and what changes in a
   concurrent or distributed version. Round 1 has a `SELF_REVIEW_AFTER.md` to check against
   afterwards; round 2 has the tickets.

Treat any AI assistant the way the round expects: use it to understand the code and sanity
-check your tests, write and own the fix yourself.

## Practising with a local AI assistant

The real rounds let you use an AI assistant. If you do not have a paid AI subscription, a
free, offline option is the
[AIInterviewPrepChat](https://marketplace.visualstudio.com/items?itemName=samthemogul.ai-interview-prep-chat)
VS Code extension by Samuel Emeka. It runs a local model through [Ollama](https://ollama.com),
so your code and conversations stay on your machine, with no accounts, API keys, or internet
connection needed.

It has two interview settings that line up with these packs:

- **Guarded** — like a standard coding test (and Bloomberg's round shape): the AI explains
  errors, concepts, and code, and only writes code for an approach you describe yourself.
  Use it to drill the "map the code, then verify" loop.
- **Unguarded (Agent)** — like a code-repos round: the agent proposes file edits as diffs
  you review and accept or reject. Use it to practise reviewing AI output like a teammate's
  pull request.

It also keeps a local practice transcript so you can review how you used the assistant
afterwards. Requires VS Code 1.90 or later and Ollama.

## Practising on real codebases in the browser

[Groundwork](https://groundwork-two-roan.vercel.app/) (beta) is a hosted version of this
same drill: "Every engineer gets a real codebase," nothing to install. You get a timed
ticket (a bug report, a failing test suite, or a small feature) pinned to a real repository,
an isolated browser-based VS Code editor and terminal with dependencies preinstalled and no
internet, and a 30 to 35 minute budget. Tasks are in TypeScript and Python (Node, Express,
Jest, pytest). On submit, hidden checks run against the behaviour the ticket describes and
the repo's existing tests run again; you get your diff, each check's pass or fail, and your
duration, with no composite score and no leaderboard.

It has a built-in AI assistant, **Pair**, that reads the repository and explains code. In
its default **guarded** mode it will not write the fix, which is exactly the Bloomberg
posture: use the assistant to understand the code, then write and own the change yourself.
You can switch it to an ordinary assistant, and that choice is recorded with the attempt.

It is free to start and needs an account. Use Groundwork for the "unfamiliar codebase under
time pressure" muscle in TypeScript and Python; use the packs in this repo when you want to
drill offline, or in C++ and Java, or rehearse the round-1 explain-out-loud flow.
