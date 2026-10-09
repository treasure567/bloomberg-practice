#include <iostream>
#include "sessions.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { SessionService s; s.create("s",0,10); check("expiry_boundary_is_inclusive", !s.valid("s",10)); }
    { SessionService s; s.create("s",0,10); s.touch("s",8,10); check("touch_refreshes_expiry", s.valid("s",15)); }
    { SessionService s; s.create("s",0,10); s.cleanup(10); check("cleanup_removes_expired", !s.valid("s",10) && s.size()==0); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
