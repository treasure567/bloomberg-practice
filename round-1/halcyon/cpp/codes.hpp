#pragma once
#include <string>
#include <set>
#include <functional>

struct Entry { std::string participant; std::string code; };

struct CodeIssuer {
    std::function<double()> rand_source;
    explicit CodeIssuer(std::function<double()> r) : rand_source(std::move(r)) {}

    Entry issue(const std::string& participant) const {
        int number = static_cast<int>(rand_source() * 100000);
        return Entry{participant, std::to_string(number)};
    }

    static int match_count(const std::string& code, const std::string& winning) {
        std::set<char> a(code.begin(), code.end());
        std::set<char> b(winning.begin(), winning.end());
        int n = 0;
        for (char c : a) if (b.count(c)) ++n;
        return n;
    }
};
