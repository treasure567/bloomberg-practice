#include <iostream>
#include <string>
#include "codes.hpp"

static int total = 0, failures = 0;
static void check(const std::string& n, bool c) { ++total; std::cout << (c ? "PASS " : (++failures, "FAIL ")) << n << "\n"; }

int main() {
    check("format_pads_and_checks", format_code(42) == "ORD-00000042-6");
    check("format_zero", format_code(0) == "ORD-00000000-0");
    check("valid_true_and_false_on_checkdigit", is_valid("ORD-00000042-6") && !is_valid("ORD-00000042-7"));
    check("invalid_when_missing_check_segment", !is_valid("ORD-00000042"));
    std::cout << (failures ? "FAILED " : "OK ") << (total - failures) << "/" << total << "\n";
    return failures ? 1 : 0;
}
