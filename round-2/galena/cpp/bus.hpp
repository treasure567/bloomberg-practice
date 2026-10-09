#pragma once
#include <string>
#include <vector>
#include <functional>
struct Subscription { int token; std::string pattern; std::function<void(const std::string&)> cb; };
struct MessageBus {
    std::vector<Subscription> subs;
    int counter = 0;
    int subscribe(const std::string& pattern, std::function<void(const std::string&)> cb) {
        int t = ++counter; subs.push_back({t, pattern, cb}); return t;
    }
    void unsubscribe(int token) {
        std::vector<Subscription> keep;
        for (auto& s : subs) if (s.pattern != std::to_string(token)) keep.push_back(s);   // BUG: compares pattern to token
        subs = keep;
    }
    bool matches(const std::string& pattern, const std::string& topic) const {
        return pattern == topic;                                                          // BUG: no wildcard support
    }
    void publish(const std::string& topic, const std::string& msg) {
        for (auto& s : subs) if (matches(s.pattern, topic)) s.cb(msg);                     // BUG: no isolation
    }
};
