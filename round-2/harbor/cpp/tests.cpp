#include <iostream>
#include <string>
#include <functional>
#include "payments.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
static void check_throws(const char* n, const std::function<void()>& f){ ++total; bool t=false; try{f();}catch(...){t=true;} std::cout<<(t?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
static PaymentsService svc(){ PaymentsService s; s.open_account("A"); s.open_account("B"); return s; }
int main(){
    { auto s=svc(); s.deposit("A",100); s.transfer("t1","A","B",40); check("transfer_moves_funds", s.balance("A")==60 && s.balance("B")==40); }
    { auto s=svc(); s.deposit("A",100); s.transfer("t1","A","B",40); s.transfer("t1","A","B",40); check("transfer_is_idempotent", s.balance("B")==40); }
    { auto s=svc(); s.deposit("A",100); s.place_hold("h1","A",40); check_throws("overdraft_rejected", [&]{ s.transfer("t1","A","B",80); }); }
    { auto s=svc(); s.deposit("A",100); s.place_hold("h1","A",30); bool a=s.available("A")==70; s.release_hold("h1"); check("release_restores_available", a && s.available("A")==100); }
    { auto s=svc(); s.deposit("A",100); s.transfer("t1","A","B",40); long sum=0; for(auto&kv:s.ledger.balances) sum+=kv.second; check("double_entry_conservation", sum==0); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
