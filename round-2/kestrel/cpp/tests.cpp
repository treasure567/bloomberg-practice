#include <iostream>
#include "matching.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { OrderBook b; b.limit("A","sell",100,5); b.limit("B","sell",100,5); auto t=b.limit("T","buy",100,5);
      check("price_time_priority_fifo", t.size()==1 && t[0].maker_id=="A"); }
    { OrderBook b; b.limit("A","sell",100,10); auto f=b.limit("T1","buy",100,4); auto s=b.limit("T2","buy",100,6);
      check("partial_fill_reduces_resting_qty", f.size()==1 && f[0].qty==4 && s.size()==1 && s[0].qty==6); }
    { OrderBook b; b.limit("A","sell",100,5); b.cancel("A"); auto t=b.limit("T","buy",100,5);
      check("cancel_removes_resting_order", t.empty()); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
