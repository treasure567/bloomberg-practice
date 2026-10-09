#include <iostream>
#include <vector>
#include "split.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
using V=std::vector<long>;
int main(){
    check("split_100_3", split_amount(100,3)==V{34,33,33});
    check("split_10_4", split_amount(10,4)==V{3,3,2,2});
    check("split_7_2", split_amount(7,2)==V{4,3});
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
