#include <iostream>
#include <algorithm>
#include "orchestration.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
static bool indead(OrchestrationService& s, const std::string& j){ auto d=s.dead_letters(); return std::find(d.begin(),d.end(),j)!=d.end(); }
int main(){
    { OrchestrationService s(3); s.enqueue("A"); auto a=s.dequeue(); check("dequeue_removes_job", a.value_or("")=="A" && !s.dequeue().has_value()); }
    { OrchestrationService s(3); s.enqueue("A"); auto j=s.dequeue(); s.ack(*j); check("ack_completes_job", !s.dequeue().has_value()); }
    { OrchestrationService s(2); s.enqueue("A"); s.nack("A"); s.nack("A"); check("two_nacks_dead_letter_at_max_2", indead(s,"A")); }
    { OrchestrationService s(1); s.enqueue("A"); s.nack("A"); check("one_nack_dead_letter_at_max_1", indead(s,"A")); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
