#pragma once
#include <string>
#include <vector>
#include <algorithm>
struct Resting { std::string order_id, side; long price, qty, seq; };
struct Trade { std::string maker_id, taker_id; long price, qty; };
struct OrderBook {
    std::vector<Resting> asks, bids;
    long seq = 0;
    long next_seq() { return ++seq; }
    void cancel(const std::string&) {}                    // BUG: no-op
    std::vector<Trade> limit(const std::string& order_id, const std::string& side, long price, long qty) {
        std::vector<Trade> trades;
        if (side == "buy") {
            std::sort(asks.begin(), asks.end(), [](const Resting& a, const Resting& b) { return a.price != b.price ? a.price < b.price : a.seq > b.seq; }); // BUG: -seq breaks FIFO
            size_t i = 0;
            while (qty > 0 && i < asks.size()) {
                if (asks[i].price <= price) {
                    long fill = std::min(qty, asks[i].qty);
                    trades.push_back({asks[i].order_id, order_id, asks[i].price, fill});
                    qty -= fill;
                    asks.erase(asks.begin() + i);          // BUG: removes whole resting order on partial fill
                } else break;
            }
            if (qty > 0) bids.push_back({order_id, "buy", price, qty, next_seq()});
        } else {
            std::sort(bids.begin(), bids.end(), [](const Resting& a, const Resting& b) { return a.price != b.price ? a.price > b.price : a.seq > b.seq; });
            size_t i = 0;
            while (qty > 0 && i < bids.size()) {
                if (bids[i].price >= price) {
                    long fill = std::min(qty, bids[i].qty);
                    trades.push_back({bids[i].order_id, order_id, bids[i].price, fill});
                    qty -= fill;
                    bids.erase(bids.begin() + i);
                } else break;
            }
            if (qty > 0) asks.push_back({order_id, "sell", price, qty, next_seq()});
        }
        return trades;
    }
};
