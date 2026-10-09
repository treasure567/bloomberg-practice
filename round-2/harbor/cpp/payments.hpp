#pragma once
#include <string>
#include <map>
#include <set>
#include <stdexcept>

struct InsufficientFunds : std::runtime_error { explicit InsufficientFunds(const std::string& m) : std::runtime_error(m) {} };

struct Ledger {
    std::map<std::string, long> balances;
    void post(const std::string&, const std::string& debit, const std::string& credit, long amount) {
        balances[debit] += amount;
        balances[credit] += amount;            // BUG: credit must subtract
    }
    long balance(const std::string& a) const { auto it = balances.find(a); return it == balances.end() ? 0 : it->second; }
};

struct Hold { std::string account; long amount; bool active; };

struct HoldBook {
    std::map<std::string, Hold> holds;
    void place(const std::string& id, const std::string& account, long amount) { holds[id] = {account, amount, true}; }
    void release(const std::string&) {}        // BUG: no-op
    long held(const std::string& account) const {
        long s = 0; for (auto& kv : holds) if (kv.second.active && kv.second.account == account) s += kv.second.amount; return s;
    }
};

struct PaymentsService {
    Ledger ledger; HoldBook holds; std::set<std::string> accounts, seen;
    PaymentsService() { accounts.insert("external"); }
    void open_account(const std::string& a) { accounts.insert(a); }
    void require(const std::string& a) { if (!accounts.count(a)) throw std::runtime_error("unknown account"); }
    void deposit(const std::string& a, long amount) { require(a); ledger.post("deposit", a, "external", amount); }
    void place_hold(const std::string& id, const std::string& a, long amount) { require(a); holds.place(id, a, amount); }
    void release_hold(const std::string& id) { holds.release(id); }
    long available(const std::string& a) const { return ledger.balance(a) - holds.held(a); }
    void transfer(const std::string& id, const std::string& src, const std::string& dst, long amount) {
        if (amount <= 0) throw std::runtime_error("amount must be positive");
        require(src); require(dst);
        ledger.post(id, dst, src, amount);     // BUG: no idempotency, no funds check
    }
    long balance(const std::string& a) const { return ledger.balance(a); }
};
