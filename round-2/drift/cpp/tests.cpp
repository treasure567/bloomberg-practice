#include <iostream>
#include <functional>
#include "fulfillment.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
static void check_throws(const char* n, const std::function<void()>& f){ ++total; bool t=false; try{f();}catch(...){t=true;} std::cout<<(t?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
static FulfillmentService svc(){ FulfillmentService s; s.add_sku("A"); s.set_stock("A",10); return s; }
int main(){
    { auto s=svc(); s.reserve("r1","A",3); check("available_reflects_reservations", s.available("A")==7); }
    { auto s=svc(); check_throws("oversell_rejected", [&]{ s.reserve("r2","A",100); }); }
    { auto s=svc(); s.reserve("r1","A",3); bool a=s.available("A")==7; s.release("r1"); check("release_restores_availability", a && s.reserved("A")==0 && s.available("A")==10); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
