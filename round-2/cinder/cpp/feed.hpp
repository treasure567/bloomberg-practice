#pragma once
#include <string>
#include <map>
#include <vector>
#include <functional>
#include <optional>
#include <stdexcept>
struct Quote { std::string symbol; long bid, ask, seq; };
struct QuoteStore {
    std::map<std::string, Quote> quotes;
    void apply(const Quote& q) { quotes[q.symbol] = q; }          // BUG: no sequence guard, accepts stale
    std::optional<Quote> get(const std::string& s) {
        auto it = quotes.find(s);
        if (it == quotes.end()) return std::nullopt;
        return it->second;
    }
};
struct SubscriptionHub {
    struct Sub { int token; std::function<void(const Quote&)> cb; };
    std::map<std::string, std::vector<Sub>> subs;
    int counter = 0;
    int subscribe(const std::string& sym, std::function<void(const Quote&)> cb) {
        int t = ++counter; subs[sym].push_back({t, cb}); return t;
    }
    void unsubscribe(const std::string& sym, int token) {
        std::vector<Sub> keep;
        for (auto& s : subs[sym]) if (s.token == token) keep.push_back(s);  // BUG: inverted, keeps the one removed
        subs[sym] = keep;
    }
    void publish(const std::string& sym, const Quote& q) {
        for (auto& s : subs[sym]) s.cb(q);                        // BUG: no isolation, one throw kills the fanout
    }
};
struct MarketDataFeed {
    QuoteStore& store;
    explicit MarketDataFeed(QuoteStore& s) : store(s) {}
    void apply_snapshot(const Quote& q) { store.apply(q); }
    void apply_delta(const std::string& sym, long seq, long bid, long ask) {
        auto cur = store.get(sym);
        long b = cur ? cur->bid : 0;                              // BUG: fabricates a 0/0 base instead of raising
        long a = cur ? cur->ask : 0;
        store.apply({sym, bid ? bid : b, ask ? ask : a, seq});
    }
};
