#pragma once
#include <vector>
inline std::vector<long> backoff_delays(long base, int attempts, long max_delay) {
    std::vector<long> out;
    for (int a = 1; a <= attempts; ++a) {
        long d = base * (1L << a);
        out.push_back(d);
    }
    return out;
}
