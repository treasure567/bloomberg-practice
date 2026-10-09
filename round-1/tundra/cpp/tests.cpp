#include <iostream>
#include "tick.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    check("rounds_up_near_tick", round_to_tick(103,5)==105);
    check("rounds_to_nearest", round_to_tick(108,5)==110);
    check("tie_rounds_up", round_to_tick(1025,50)==1050);
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
