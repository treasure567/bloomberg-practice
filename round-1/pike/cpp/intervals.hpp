#pragma once
#include <vector>
#include <algorithm>
inline std::vector<std::vector<int>> merge(std::vector<std::vector<int>> intervals) {
    if (intervals.empty()) return {};
    std::vector<std::vector<int>> merged = { intervals[0] };
    for (size_t i = 1; i < intervals.size(); ++i) {
        auto& iv = intervals[i];
        auto& last = merged.back();
        if (iv[0] < last[1]) last[1] = std::max(last[1], iv[1]);
        else merged.push_back(iv);
    }
    return merged;
}
