import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Scheduling.Database db=new Scheduling.Database(); Scheduling.MeetingRequest r=new Scheduling.MeetingRequest();
          r.requestId="r1"; r.requesterKey="u1"; r.idempotencyKey="k1"; db.insertRequest(r);
          boolean raised=false; try { db.insertRequest(r); } catch(RuntimeException e){ raised=true; }
          check("db_enforces_idempotency_uniqueness", raised); }
        { List<Scheduling.CalendarEvent> ev=Arrays.asList(new Scheduling.CalendarEvent("e1",600,660,true));
          Scheduling.MeetingRequest r=new Scheduling.MeetingRequest(); r.requestId="r1"; r.start=600; r.end=660; r.tier=Scheduling.Tier.STANDARD; r.submittedAt=1;
          List<Scheduling.MeetingRequest> out=Scheduling.scheduleBatch(Arrays.asList(r), ev); check("scheduler_respects_protected_events", out.isEmpty()); }
        { Scheduling.MeetingRequest ex=new Scheduling.MeetingRequest(); ex.requestId="ex"; ex.start=600; ex.end=660; ex.tier=Scheduling.Tier.EXECUTIVE; ex.submittedAt=1;
          Scheduling.MeetingRequest st=new Scheduling.MeetingRequest(); st.requestId="st"; st.start=600; st.end=660; st.tier=Scheduling.Tier.STANDARD; st.submittedAt=5;
          List<Scheduling.MeetingRequest> out=Scheduling.scheduleBatch(Arrays.asList(ex,st), new ArrayList<>());
          check("scorer_prioritises_business_tier", out.size()==1 && out.get(0).requestId.equals("ex")); }
        { Scheduling.Database db=new Scheduling.Database(); Scheduling.MeetingRequest r=new Scheduling.MeetingRequest(); r.requestId="r1"; db.insertRequest(r);
          Scheduling.SchedulingService svc=new Scheduling.SchedulingService(db); svc.reject("r1");
          boolean raised=false; try { svc.accept("r1"); } catch(RuntimeException e){ raised=true; }
          check("rejected_cannot_be_accepted", raised); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
