#include <iostream>
#include <vector>
#include "stats.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    check("moving_average_basic", moving_average({1,2,3,4},2) == std::vector<double>({1.5,2.5,3.5}));
    check("moving_average_full_window", moving_average({2,4,6},3) == std::vector<double>({4.0}));
    check("rolling_max", rolling_max({1,3,2,5,4},2) == std::vector<long>({3,3,5,5}));
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
