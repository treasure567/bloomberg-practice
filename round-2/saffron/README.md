# Session Service

Welcome to the team that owns sessions. A session store keeps sessions keyed by id; an expiry
policy decides when a session is dead; sessions can be refreshed and expired ones cleaned up.
Times are integer ticks.

This repository has three reported problems in `tickets/`. Your interviewer will tell you which
ticket to start with. You are not expected to finish every ticket.

You may use the available AI assistant and normal repository tools. Treat the assistant like a
junior developer: establish a plan, inspect its work, run the tests, and retain ownership of the
result.

## Run the tests

This pack has the same problem in three languages (`python/`, `cpp/`, `java/`). Pick one:

```bash
# Python
cd python && pytest -q

# C++
cd cpp && make test          # or: g++ -std=c++17 tests.cpp -o tests && ./tests

# Java
cd java && javac *.java && java Tests
```

All three implement the same spec and the same planted bugs; every test fails until you fix them.

## Repository map

```text
sessions/
  models.py    domain types (Session: sid, expiry, data)
  errors.py    SessionError
  expiry.py    ExpiryPolicy: is_expired(session, now)
  store.py     SessionStore: put / get / delete / all / size
  service.py   SessionService: create / get / touch / cleanup / size
tests/         shipped regression tests
tickets/       reported work
```

## Product rules already agreed

- a session is expired once the clock reaches its expiry tick: `now >= expiry`;
- a valid `get` returns the session data; an expired one returns nothing;
- `touch` extends a session's life to `now + ttl`;
- `cleanup` reclaims expired sessions so the store does not grow without bound.
