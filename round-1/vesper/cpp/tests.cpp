#include <iostream>
#include <vector>
#include "backoff.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
using V=std::vector<long>;
int main(){
    check("exponential_growth", backoff_delays(1,4,100)==V{1,2,4,8});
    check("capped_at_max", backoff_delays(1,5,5)==V{1,2,4,5,5});
    check("nonunit_base", backoff_delays(3,3,100)==V{3,6,12});
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
