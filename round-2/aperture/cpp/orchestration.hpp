#pragma once
#include <string>
#include <vector>
#include <map>
#include <optional>
struct OrchestrationService {
    int max_retries;
    std::vector<std::string> ready;
    std::map<std::string, int> attempts;
    std::vector<std::string> dead;
    explicit OrchestrationService(int mr) : max_retries(mr) {}
    void enqueue(const std::string& j) { attempts[j] = 0; ready.push_back(j); }
    std::optional<std::string> dequeue() {
        if (ready.empty()) return std::nullopt;
        return ready.front();                       // BUG: peeks, does not remove
    }
    void ack(const std::string&) {}                 // BUG: does not remove the job
    void nack(const std::string& j) {
        for (size_t i = 0; i < ready.size(); ++i) if (ready[i] == j) { ready.erase(ready.begin() + i); break; }
        if (attempts[j] > max_retries) dead.push_back(j);   // BUG: no attempts++, and > should be >=
        else ready.push_back(j);
    }
    std::vector<std::string> dead_letters() { return dead; }
};
