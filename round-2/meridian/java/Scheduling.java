import java.util.*;
public class Scheduling {
    public enum Tier { STANDARD(1), PRIORITY(2), EXECUTIVE(3); public final int w; Tier(int w){this.w=w;} }
    public enum Status { PENDING, ACCEPTED, REJECTED }
    public static class MeetingRequest {
        public String requestId, requesterKey, idempotencyKey;
        public long start, end, submittedAt;
        public Tier tier = Tier.STANDARD;
        public Status status = Status.PENDING;
    }
    public static class CalendarEvent { public String eventId; public long start, end; public boolean isProtected;
        public CalendarEvent(String i,long s,long e,boolean p){eventId=i;start=s;end=e;isProtected=p;} }
    public static class Database {
        List<MeetingRequest> requests = new ArrayList<>();
        public void insertRequest(MeetingRequest r){ requests.add(r); }           // BUG no uniqueness
        public MeetingRequest get(String id){ for(MeetingRequest r: requests) if(r.requestId.equals(id)) return r; return null; }
        public void setStatus(String id, Status s){ MeetingRequest r=get(id); if(r!=null) r.status=s; }
    }
    static long[] score(MeetingRequest r){ return new long[]{ r.submittedAt, 0 }; }  // BUG ignores tier
    static boolean overlaps(long a0,long a1,long b0,long b1){ return a0<b1 && b0<a1; }
    public static List<MeetingRequest> scheduleBatch(List<MeetingRequest> reqs, List<CalendarEvent> events){
        reqs = new ArrayList<>(reqs);
        reqs.sort((a,b)->{ long[] sa=score(a), sb=score(b); if(sa[0]!=sb[0]) return Long.compare(sb[0],sa[0]); return Long.compare(sb[1],sa[1]); });
        List<long[]> booked = new ArrayList<>();                                   // BUG does not seed protected events
        List<MeetingRequest> scheduled = new ArrayList<>();
        for(MeetingRequest r: reqs){
            boolean conflict=false;
            for(long[] b: booked) if(overlaps(r.start,r.end,b[0],b[1])){ conflict=true; break; }
            if(conflict) continue;
            booked.add(new long[]{r.start,r.end}); scheduled.add(r);
        }
        return scheduled;
    }
    public static class SchedulingService {
        Database db;
        public SchedulingService(Database d){ db=d; }
        public void accept(String id){ db.setStatus(id, Status.ACCEPTED); }        // BUG no terminal guard
        public void reject(String id){ db.setStatus(id, Status.REJECTED); }
    }
}
