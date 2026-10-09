#include <iostream>
#include "cache.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { LRUCache c(2); c.put("a",1); c.put("b",2); c.put("c",3);
      check("evicts_least_recently_used", !c.get("a").has_value() && c.get("b").value_or(-1)==2 && c.get("c").value_or(-1)==3); }
    { LRUCache c(2); c.put("a",1); c.put("b",2); c.get("a"); c.put("c",3);
      check("get_refreshes_recency", c.get("a").value_or(-1)==1 && !c.get("b").has_value()); }
    { LRUCache c(2); c.put("a",1); c.put("b",2); c.put("a",9); c.put("c",3);
      check("update_existing_refreshes_without_growth", c.get("a").value_or(-1)==9 && !c.get("b").has_value()); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
