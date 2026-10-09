#include <iostream>
#include <vector>
#include <string>
#include "bus.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { MessageBus b; std::vector<std::string> got; b.subscribe("px.*", [&](const std::string& m){ got.push_back(m); });
      b.publish("px.AAPL","hi"); check("wildcard_segment_match", got.size()==1 && got[0]=="hi"); }
    { MessageBus b; std::vector<std::string> got; int t=b.subscribe("px.AAPL", [&](const std::string& m){ got.push_back(m); });
      b.unsubscribe(t); b.publish("px.AAPL","hi"); check("unsubscribe_stops_delivery", got.empty()); }
    { MessageBus b; std::vector<std::string> got;
      b.subscribe("px.AAPL", [](const std::string&){ throw std::runtime_error("boom"); });
      b.subscribe("px.AAPL", [&](const std::string& m){ got.push_back(m); });
      try { b.publish("px.AAPL","hi"); } catch(...) {}
      check("raising_subscriber_does_not_block_others", got.size()==1 && got[0]=="hi"); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
