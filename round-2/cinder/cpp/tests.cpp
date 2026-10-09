#include <iostream>
#include <vector>
#include "feed.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { QuoteStore s; s.apply({"AAPL",110,111,2}); s.apply({"AAPL",100,101,1});
      auto q=s.get("AAPL"); check("store_ignores_stale_seq", q && q->seq==2 && q->bid==110); }
    { SubscriptionHub h; int got=0; int t=h.subscribe("AAPL",[&](const Quote&){ got++; }); h.unsubscribe("AAPL",t);
      h.publish("AAPL",{"AAPL",100,101,1}); check("unsubscribe_stops_callbacks", got==0); }
    { SubscriptionHub h; std::vector<long> got;
      h.subscribe("AAPL",[&](const Quote&){ throw std::runtime_error("boom"); });
      h.subscribe("AAPL",[&](const Quote& q){ got.push_back(q.bid); });
      try { h.publish("AAPL",{"AAPL",100,101,1}); } catch(...) {}
      check("publish_isolates_subscriber_errors", got.size()==1 && got[0]==100); }
    { QuoteStore s; MarketDataFeed f(s); bool raised=false;
      try { f.apply_delta("AAPL",1,100,101); } catch(const std::exception&){ raised=true; }
      check("delta_before_snapshot_raises", raised); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
