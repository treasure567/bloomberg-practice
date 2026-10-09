# bloomberg-practice

Interview-grade practice for Bloomberg's AI-assisted codebase rounds. Each pack is an
**unfamiliar codebase** under a codename that reveals nothing about the domain. Read the pack's
`README.md` and `tickets/`, map the modules, find the deliberately planted bugs, and make the test
suite pass with the smallest changes.

- `round-1/` — a focused service: a few interacting modules, tickets, and tests. Target ~35 minutes.
- `round-2/` — a larger multi-module **microservice** (models, persistence, domain logic,
  orchestration) with a backlog of tickets. Target ~45 minutes.

Every pack ships with **all tests failing by default** — the code has deliberately planted bugs,
tuned harder than the real round. There are no solutions in the repository; a green suite is the
proof you fixed it.

## Languages

Each pack keeps its **spec and tickets shared** (they are language-agnostic) and the code lives in
a per-language subfolder:

```text
round-1/halcyon/
  README.md    shared: spec, product rules, how to run each language
  tickets/     shared: the reported problems
  python/      Python implementation + tests   (pytest)
  cpp/         C++ implementation + tests       (g++, make test)
  java/        Java implementation + tests      (javac / java Tests)
```

- **Round 1** is available in **Python, C++, and Java** — same problem, same planted bugs, pick
  your language.
- **Round 2** is available in **Python, C++, and Java** too — same spec and the same planted bugs
  across all three.

Quick run:

```bash
cd round-1/halcyon/python && pytest -q      # or ../cpp && make test, or ../java && javac *.java && java Tests
cd round-2/harbor/python && pytest -q
```

To add your own packs or a language port, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Round 1 — focused services (~35 min, Python / C++ / Java)

| Pack | Service | What it is |
| --- | --- | --- |
| [halcyon](round-1/halcyon) | Pooled Draw | 5-digit entry codes and tiered payout distribution for a pooled cash drawing. |
| [marlin](round-1/marlin) | Trade Settlement | Per-symbol positions and realized PnL settled from a batch of fills. |
| [zephyr](round-1/zephyr) | Order Identifiers | Zero-padded order codes with a trailing check digit, and validation. |
| [cobalt](round-1/cobalt) | Rolling Statistics | Moving averages and rolling maxima over a sliding window. |
| [quasar](round-1/quasar) | Fee Calculation | Tiered transaction fees with a minimum-fee floor. |
| [onyx](round-1/onyx) | Rate Limiter | A fixed-window rate limiter. |
| [pike](round-1/pike) | Interval Merge | Merge overlapping and touching intervals, sorted output. |
| [vesper](round-1/vesper) | Retry Backoff | Exponential retry backoff delays, capped at a maximum. |
| [tundra](round-1/tundra) | Tick Rounding | Round a price to the nearest tick size, ties up. |
| [lumen](round-1/lumen) | Amount Split | Split a total among n recipients, remainder to the earliest. |

## Round 2 — microservices (~45 min, Python / C++ / Java)

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
2. Read the pack `README.md` (product rules) and the `tickets/` (reported problems).
3. Run the tests — all red. Map the modules, isolate a bug with a failing test, patch the
   narrowest layer, and turn the suite green.
4. Narrate your reasoning the whole time, and use an AI assistant the way the round expects:
   plan, inspect its output, verify in the code, and keep ownership of the result.

## Practising with a local AI assistant

The real rounds let you use an AI assistant. If you do not have a paid AI subscription, a free,
offline option is the
[AIInterviewPrepChat](https://marketplace.visualstudio.com/items?itemName=samthemogul.ai-interview-prep-chat)
VS Code extension by Samuel Emeka. It runs a local model through [Ollama](https://ollama.com), so
your code and conversations stay on your machine, with no accounts, API keys, or internet
connection needed.

It has two interview settings that line up with these packs:

- **Guarded** — like a standard coding test (and Bloomberg's round shape): the AI explains errors,
  concepts, and code, and only writes code for an approach you describe yourself. Use it to drill
  the "map the code, then verify" loop.
- **Unguarded (Agent)** — like a code-repos round: the agent proposes file edits as diffs you
  review and accept or reject. Use it to practise reviewing AI output like a teammate's pull
  request.

It also keeps a local practice transcript so you can review how you used the assistant afterwards.
Requires VS Code 1.90 or later and Ollama.
