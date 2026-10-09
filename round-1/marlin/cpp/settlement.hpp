#pragma once
#include <string>
#include <map>
#include <set>
#include <vector>
#include <stdexcept>

struct Position { long quantity = 0, cost_basis_cents = 0, last_price_cents = 0; };
struct Fill { std::string trade_id, symbol, side; long quantity, price_cents; };

struct Blotter {
    std::map<std::string, Position> positions;
    long realized_pnl_cents = 0;
    std::set<std::string> seen;

    void apply(const Fill& f) {
        Position& pos = positions[f.symbol];
        if (f.side == "buy") {
            pos.quantity += f.quantity;
            pos.cost_basis_cents += f.quantity * f.price_cents;
            pos.last_price_cents = f.price_cents;
        } else {
            double avg = static_cast<double>(pos.cost_basis_cents) / pos.quantity;
            realized_pnl_cents += (f.price_cents - pos.last_price_cents) * f.quantity;
            pos.quantity -= f.quantity;
            pos.cost_basis_cents -= static_cast<long>(avg * f.quantity);
        }
    }
};

inline Blotter settle(const std::vector<Fill>& fills) {
    Blotter b;
    for (const auto& f : fills) b.apply(f);
    return b;
}
