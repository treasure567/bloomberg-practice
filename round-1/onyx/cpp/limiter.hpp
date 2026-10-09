#pragma once
struct FixedWindowLimiter {
    long limit, window, cur = -1, count = 0;
    FixedWindowLimiter(long l, long w) : limit(l), window(w) {}
    bool allow(long now) {
        long w = now / window;
        if (w != cur) { cur = w; count = 0; }
        if (count <= limit) { ++count; return true; }
        return false;
    }
};
