#include <iostream>
#include "risk.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { RiskService s; s.add_trade("t1","cpA","X",10); s.add_trade("t2","cpA","X",-4); check("signed_netting", s.net_position("cpA","X")==6); }
    { RiskService s; s.add_trade("t1","cpA","X",10); s.add_trade("t1","cpA","X",10); check("idempotent_on_trade_id", s.net_position("cpA","X")==10); }
    { RiskService s; s.add_trade("t1","cpA","X",10); s.add_trade("t2","cpB","X",5); check("counterparties_isolated", s.net_position("cpA","X")==10 && s.net_position("cpB","X")==5); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
