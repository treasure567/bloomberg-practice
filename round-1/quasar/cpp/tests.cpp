#include <iostream>
#include "fees.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    check("min_fee_floor", fee_for(2000)==50);
    check("boundary_10000_is_one_percent", fee_for(10000)==100);
    check("boundary_100000_is_half_percent", fee_for(100000)==500);
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
