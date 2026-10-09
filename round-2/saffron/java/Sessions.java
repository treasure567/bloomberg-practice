import java.util.*;
public class Sessions {
    static class Session { long expiry; Session(long e){expiry=e;} }
    Map<String,Session> sessions=new HashMap<>();
    public void create(String sid,long now,long ttl){ sessions.put(sid,new Session(now+ttl)); }
    boolean isExpired(Session s,long now){ return now > s.expiry; }          // BUG >=
    public boolean valid(String sid,long now){ Session s=sessions.get(sid); if(s==null) return false; return !isExpired(s,now); }
    public void touch(String sid,long now,long ttl){}                        // BUG no-op
    public void cleanup(long now){}                                          // BUG no-op
    public int size(){ return sessions.size(); }
}
