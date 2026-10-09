#pragma once
#include <string>
#include <map>
struct Session { long expiry; };
struct SessionService {
    std::map<std::string, Session> sessions;
    void create(const std::string& sid, long now, long ttl) { sessions[sid] = {now + ttl}; }
    bool is_expired(const Session& s, long now) const { return now > s.expiry; }   // BUG: should be >=
    bool valid(const std::string& sid, long now) {
        auto it = sessions.find(sid);
        if (it == sessions.end()) return false;
        return !is_expired(it->second, now);
    }
    void touch(const std::string&, long, long) {}                                   // BUG: no-op
    void cleanup(long) {}                                                           // BUG: no-op
    int size() const { return (int)sessions.size(); }
};
