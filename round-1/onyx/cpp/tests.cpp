#include <iostream>
#include "limiter.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { FixedWindowLimiter l(2,10); check("blocks_after_limit", l.allow(0)&&l.allow(1)&&!l.allow(2)); }
    { FixedWindowLimiter l(2,10); bool a=l.allow(0),b=l.allow(1),c=l.allow(2),d=l.allow(10);
      check("resets_next_window", a&&b&&!c&&d); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
