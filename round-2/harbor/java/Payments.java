import java.util.*;
public class Payments {
    public static class InsufficientFunds extends RuntimeException { InsufficientFunds(String m){ super(m);} }
    static class Ledger {
        Map<String,Long> bal = new HashMap<>();
        void post(String t, String debit, String credit, long amount){ bal.merge(debit, amount, Long::sum); bal.merge(credit, amount, Long::sum); }
        long balance(String a){ return bal.getOrDefault(a, 0L); }
    }
    static class Hold { String account; long amount; boolean active; Hold(String a,long m){account=a;amount=m;active=true;} }
    static class HoldBook {
        Map<String,Hold> holds = new HashMap<>();
        void place(String id,String a,long m){ holds.put(id,new Hold(a,m)); }
        void release(String id){}
        long held(String a){ long s=0; for(Hold h:holds.values()) if(h.active&&h.account.equals(a)) s+=h.amount; return s; }
    }
    Ledger ledger=new Ledger(); HoldBook holds=new HoldBook(); Set<String> accounts=new HashSet<>(), seen=new HashSet<>();
    public Payments(){ accounts.add("external"); }
    public void openAccount(String a){ accounts.add(a); }
    void require(String a){ if(!accounts.contains(a)) throw new RuntimeException("unknown account"); }
    public void deposit(String a,long amt){ require(a); ledger.post("deposit",a,"external",amt); }
    public void placeHold(String id,String a,long amt){ require(a); holds.place(id,a,amt); }
    public void releaseHold(String id){ holds.release(id); }
    public long available(String a){ return ledger.balance(a)-holds.held(a); }
    public void transfer(String id,String src,String dst,long amt){ if(amt<=0) throw new RuntimeException("amount"); require(src); require(dst); ledger.post(id,dst,src,amt); }
    public long balance(String a){ return ledger.balance(a); }
    public Map<String,Long> balances(){ return ledger.bal; }
}
