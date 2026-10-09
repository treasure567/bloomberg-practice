#pragma once
#include <string>

inline int check_digit(const std::string& body) {
    int s = 0;
    for (char c : body) s += (c - '0');
    return s % 10;
}

inline std::string format_code(int seq) {
    std::string body = std::to_string(seq);
    return "ORD-" + body + "-" + std::to_string(check_digit(body));
}

inline bool is_valid(const std::string& code) {
    return code.rfind("ORD-", 0) == 0;
}
