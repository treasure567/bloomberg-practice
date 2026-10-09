import java.util.*;
public class Fulfillment {
    public static class OutOfStock extends RuntimeException { OutOfStock(String m){ super(m);} }
    static class Reservation { String sku; long qty; boolean active; Reservation(String s,long q){sku=s;qty=q;active=true;} }
    Map<String,Long> onHand=new HashMap<>();
    Set<String> catalog=new HashSet<>();
    Map<String,Reservation> reservations=new HashMap<>();
    public void addSku(String s){ catalog.add(s); }
    public void setStock(String s,long q){ onHand.put(s,q); }
    void require(String s){ if(!catalog.contains(s)) throw new RuntimeException("unknown sku"); }
    public long reserved(String s){ long t=0; for(Reservation r:reservations.values()) if(r.active&&r.sku.equals(s)) t+=r.qty; return t; }
    public long available(String s){ return onHand.getOrDefault(s,0L); }
    public void reserve(String id,String s,long q){ if(q<=0) throw new RuntimeException("qty"); require(s); reservations.put(id,new Reservation(s,q)); }
    public void release(String id){}
}
