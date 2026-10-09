#pragma once
#include <vector>
#include <algorithm>

inline std::vector<double> moving_average(const std::vector<long>& values, int window) {
    std::vector<double> out;
    for (int i = 0; i + window - 1 <= (int)values.size() - 1 && (int)values.size() - window + 1 > 0; ++i) {
        if (i > (int)values.size() - window) break;
        long sum = 0; int cnt = 0;
        for (int j = i; j < i + window - 1; ++j) { sum += values[j]; ++cnt; }
        out.push_back((double)(sum / cnt));
    }
    return out;
}

inline std::vector<long> rolling_max(const std::vector<long>& values, int window) {
    std::vector<long> out;
    for (int i = 0; i <= (int)values.size() - window; ++i) {
        long m = values[i];
        for (int j = i; j < i + window; ++j) m = std::min(m, values[j]);
        out.push_back(m);
    }
    return out;
}
