#include <iostream>
#include <vector>
#include <string>
#include "codes.hpp"
#include "payouts.hpp"

static int total = 0, failures = 0;
static void check(const std::string& name, bool cond) {
    ++total;
    if (cond) std::cout << "PASS " << name << "\n";
    else { ++failures; std::cout << "FAIL " << name << "\n"; }
}

int main() {
    check("code_zero_is_five_zeros", CodeIssuer([]{ return 0.0; }).issue("Mina").code == "00000");
    check("code_preserves_leading_zeros", CodeIssuer([]{ return 0.00042; }).issue("Mina").code == "00042");

    {
        std::vector<Entry> e{{"Ada", "54321"}};
        auto r = distribute(e, "12345", CodeIssuer::match_count);
        bool ada = false;
        for (auto& p : r.payouts) if (p.participant == "Ada") ada = true;
        check("match_is_positional", !ada);
    }
    {
        std::vector<Entry> e{{"Win", "12345"}, {"Two", "12000"}};
        auto r = distribute(e, "12345", CodeIssuer::match_count);
        long win = -1; bool two = false;
        for (auto& p : r.payouts) { if (p.participant == "Win") win = p.amount_cents; if (p.participant == "Two") two = true; }
        check("five_match_consumes_pot", win == r.pot_cents && !two);
    }
    {
        std::vector<Entry> e{{"X", "12000"}, {"Y", "12000"}, {"Z", "12000"}};
        auto r = distribute(e, "12999", CodeIssuer::match_count);
        long t2 = 0;
        for (auto& p : r.payouts) if (p.match_count == 2) t2 += p.amount_cents;
        check("tier_split_conserves_cents", t2 == r.pot_cents * 5 / 100);
    }

    std::cout << (failures ? "FAILED " : "OK ") << (total - failures) << "/" << total << "\n";
    return failures ? 1 : 0;
}
