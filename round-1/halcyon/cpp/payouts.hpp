#pragma once
#include <string>
#include <vector>
#include <map>
#include <functional>
#include "codes.hpp"

const long POT_SEED_CENTS = 1000000;
const long ENTRY_FEE_CENTS = 500;

struct Payout { std::string participant; int match_count; long amount_cents; };
struct DrawResult { long pot_cents; std::vector<Payout> payouts; long rollover_cents; };

inline long pot_cents(int entry_count) {
    return POT_SEED_CENTS + ENTRY_FEE_CENTS * entry_count;
}

inline DrawResult distribute(const std::vector<Entry>& entries, const std::string& winning,
                             const std::function<int(const std::string&, const std::string&)>& matcher) {
    long pot = pot_cents(static_cast<int>(entries.size()));
    std::map<int, std::vector<Entry>> by_tier;
    for (const auto& e : entries) {
        int m = matcher(e.code, winning);
        if (m >= 2) by_tier[m].push_back(e);
    }
    std::map<int, int> tier_percent = {{5, 100}, {4, 40}, {3, 20}, {2, 5}};
    std::vector<Payout> payouts;
    long awarded = 0;
    for (int tier : {2, 3, 4, 5}) {
        auto it = by_tier.find(tier);
        if (it == by_tier.end()) continue;
        long amount = pot * tier_percent[tier] / 100;
        double share = static_cast<double>(amount) / it->second.size();
        for (const auto& w : it->second) {
            payouts.push_back(Payout{w.participant, tier, static_cast<long>(share)});
            awarded += static_cast<long>(share);
        }
    }
    return DrawResult{pot, payouts, pot - awarded};
}
