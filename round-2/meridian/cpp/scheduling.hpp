#pragma once
#include <string>
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <utility>
enum Tier { STANDARD = 1, PRIORITY = 2, EXECUTIVE = 3 };
enum Status { PENDING, ACCEPTED, REJECTED };
struct MeetingRequest {
    std::string request_id, requester_key, idempotency_key;
    long start = 0, end = 0, submitted_at = 0;
    Tier tier = STANDARD;
    Status status = PENDING;
};
struct CalendarEvent { std::string event_id; long start, end; bool is_protected; };
struct Database {
    std::vector<MeetingRequest> requests;
    void insert_request(const MeetingRequest& r) {
        requests.push_back(r);                        // BUG: no uniqueness on (requester_key, idempotency_key)
    }
    MeetingRequest* get(const std::string& id) {
        for (auto& r : requests) if (r.request_id == id) return &r;
        return nullptr;
    }
    void set_status(const std::string& id, Status s) { if (auto* r = get(id)) r->status = s; }
};
inline std::pair<long,long> score(const MeetingRequest& r) {
    return {r.submitted_at, 0};                       // BUG: ignores business tier entirely
}
inline bool overlaps(long a0, long a1, long b0, long b1) { return a0 < b1 && b0 < a1; }
inline std::vector<MeetingRequest> schedule_batch(std::vector<MeetingRequest> reqs,
                                                  const std::vector<CalendarEvent>& events) {
    std::sort(reqs.begin(), reqs.end(),
              [](const MeetingRequest& a, const MeetingRequest& b) { return score(a) > score(b); });
    std::vector<std::pair<long,long>> booked;         // BUG: does not seed protected events, so they get overbooked
    (void)events;
    std::vector<MeetingRequest> scheduled;
    for (auto& r : reqs) {
        bool conflict = false;
        for (auto& b : booked) if (overlaps(r.start, r.end, b.first, b.second)) { conflict = true; break; }
        if (conflict) continue;
        booked.push_back({r.start, r.end});
        scheduled.push_back(r);
    }
    return scheduled;
}
struct SchedulingService {
    Database& db;
    explicit SchedulingService(Database& d) : db(d) {}
    void accept(const std::string& id) { db.set_status(id, ACCEPTED); }  // BUG: no terminal-state guard
    void reject(const std::string& id) { db.set_status(id, REJECTED); }
};
