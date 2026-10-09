#pragma once
#include <string>
#include <list>
#include <unordered_map>
#include <optional>
struct LRUCache {
    int capacity;
    std::list<std::pair<std::string, long>> items;   // front = most recently inserted
    std::unordered_map<std::string, std::list<std::pair<std::string, long>>::iterator> idx;
    explicit LRUCache(int c) : capacity(c) {}
    std::optional<long> get(const std::string& k) {
        auto it = idx.find(k);
        if (it == idx.end()) return std::nullopt;
        return it->second->second;                   // BUG: does not refresh recency
    }
    void put(const std::string& k, long v) {
        auto it = idx.find(k);
        if (it != idx.end()) { it->second->second = v; }   // BUG: update does not refresh recency
        else { items.push_front({k, v}); idx[k] = items.begin(); }
        if ((int)items.size() > capacity) {
            auto victim = items.front();              // BUG: evicts most-recent instead of LRU
            idx.erase(victim.first);
            items.pop_front();
        }
    }
};
