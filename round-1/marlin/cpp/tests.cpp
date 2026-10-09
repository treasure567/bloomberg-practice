#include <iostream>
#include <string>
#include <vector>
#include <functional>
#include "settlement.hpp"

static int total = 0, failures = 0;
static void check(const std::string& n, bool c) { ++total; std::cout << (c ? "PASS " : (++failures, "FAIL ")) << n << "\n"; }
static void check_throws(const std::string& n, const std::function<void()>& f) {
    ++total; bool threw = false;
    try { f(); } catch (...) { threw = true; }
    std::cout << (threw ? "PASS " : (++failures, "FAIL ")) << n << "\n";
}
static Fill buy(std::string t, std::string s, long q, long p) { return {t, s, "buy", q, p}; }
static Fill sell(std::string t, std::string s, long q, long p) { return {t, s, "sell", q, p}; }

int main() {
    {
        auto b = settle({buy("1", "AAPL", 10, 10000), buy("1", "AAPL", 10, 10000)});
        check("duplicate_trade_id_applied_once", b.positions["AAPL"].quantity == 10);
    }
    {
        auto b = settle({buy("1", "AAPL", 10, 10000), buy("2", "AAPL", 10, 20000), sell("3", "AAPL", 10, 18000)});
        check("realized_pnl_uses_average_cost", b.realized_pnl_cents == 30000);
    }
    check_throws("oversell_raises", [] { Blotter b; b.apply(sell("1", "AAPL", 5, 10000)); });
    check_throws("malformed_fill_raises", [] { Blotter b; b.apply(buy("1", "A", 0, 100)); });

    std::cout << (failures ? "FAILED " : "OK ") << (total - failures) << "/" << total << "\n";
    return failures ? 1 : 0;
}
