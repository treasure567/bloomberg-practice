#include <iostream>
#include <vector>
#include "intervals.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
using V = std::vector<std::vector<int>>;
int main(){
    check("merge_unsorted_overlaps", merge(V{{1,3},{2,4},{8,10},{4,6}}) == V{{1,6},{8,10}});
    check("touching_intervals_merge", merge(V{{1,2},{2,3}}) == V{{1,3}});
    check("output_sorted", merge(V{{5,6},{1,2}}) == V{{1,2},{5,6}});
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
