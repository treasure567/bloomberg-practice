#pragma once
#include <vector>
inline std::vector<long> split_amount(long total_cents, int n) {
    long each = (long)((double)total_cents / n);
    return std::vector<long>(n, each);
}
