#pragma once
#include <string>
#include <map>
#include <stdexcept>
struct OutOfStock : std::runtime_error { explicit OutOfStock(const std::string& m) : std::runtime_error(m) {} };
struct Reservation { std::string sku; long qty; bool active; };
struct FulfillmentService {
    std::map<std::string,long> on_hand;
    std::map<std::string,bool> catalog;
    std::map<std::string,Reservation> reservations;
    void add_sku(const std::string& s) { catalog[s] = true; }
    void set_stock(const std::string& s, long q) { on_hand[s] = q; }
    void require(const std::string& s) { if (!catalog.count(s)) throw std::runtime_error("unknown sku"); }
    long reserved(const std::string& s) const { long t=0; for (auto& kv:reservations) if (kv.second.active && kv.second.sku==s) t+=kv.second.qty; return t; }
    long available(const std::string& s) const { auto it=on_hand.find(s); return it==on_hand.end()?0:it->second; }  // BUG ignores reservations
    void reserve(const std::string& id, const std::string& s, long q) {
        if (q <= 0) throw std::runtime_error("qty");
        require(s);
        reservations[id] = {s, q, true};        // BUG: no availability check
    }
    void release(const std::string&) {}          // BUG: no-op
};
