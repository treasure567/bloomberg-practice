# Message Bus

Welcome to the team that runs the internal message bus. Subscribers register a topic pattern and a
callback; publishing a message delivers it to every matching subscriber. A pattern is an exact
topic (`"px.AAPL"`), a trailing one-segment wildcard (`"px.*"`), or the match-all pattern (`"*"`).

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
bus/
  models.py         domain types (Subscription)
  errors.py         BusError
  topics.py         TopicMatcher: pattern/topic matching
  subscriptions.py  SubscriptionRegistry: add / remove / all
  router.py         Router: publish -> match -> deliver
  service.py        MessageBus: subscribe / unsubscribe / publish
tests/              shipped regression tests
tickets/            reported work
```

## Product rules already agreed

- patterns are exact, a trailing one-segment wildcard (`"a.*"`), or match-all (`"*"`);
- unsubscribing stops delivery and removes the subscription;
- one subscriber's failure must not stop delivery to the others.
