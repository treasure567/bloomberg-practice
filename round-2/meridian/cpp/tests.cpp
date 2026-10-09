#include <iostream>
#include "scheduling.hpp"
static int total=0, failures=0;
static void check(const char* n, bool c){ ++total; std::cout<<(c?"PASS ":(++failures,"FAIL "))<<n<<"\n"; }
int main(){
    { Database db; MeetingRequest r; r.request_id="r1"; r.requester_key="u1"; r.idempotency_key="k1"; db.insert_request(r);
      bool raised=false; try { db.insert_request(r); } catch(const std::exception&){ raised=true; }
      check("db_enforces_idempotency_uniqueness", raised); }
    { std::vector<CalendarEvent> ev{{"e1",600,660,true}};
      MeetingRequest r; r.request_id="r1"; r.start=600; r.end=660; r.tier=STANDARD; r.submitted_at=1;
      auto out=schedule_batch({r}, ev); check("scheduler_respects_protected_events", out.empty()); }
    { MeetingRequest ex; ex.request_id="ex"; ex.start=600; ex.end=660; ex.tier=EXECUTIVE; ex.submitted_at=1;
      MeetingRequest st; st.request_id="st"; st.start=600; st.end=660; st.tier=STANDARD; st.submitted_at=5;
      auto out=schedule_batch({ex,st}, {}); check("scorer_prioritises_business_tier", out.size()==1 && out[0].request_id=="ex"); }
    { Database db; MeetingRequest r; r.request_id="r1"; db.insert_request(r); SchedulingService svc(db);
      svc.reject("r1"); bool raised=false; try { svc.accept("r1"); } catch(const std::exception&){ raised=true; }
      check("rejected_cannot_be_accepted", raised); }
    std::cout<<(failures?"FAILED ":"OK ")<<(total-failures)<<"/"<<total<<"\n"; return failures?1:0;
}
