import java.util.*;
public class Matching {
    public static class Resting { String orderId, side; long price, qty, seq; Resting(String o,String s,long p,long q,long sq){orderId=o;side=s;price=p;qty=q;seq=sq;} }
    public static class Trade { public String makerId, takerId; public long price, qty; Trade(String m,String t,long p,long q){makerId=m;takerId=t;price=p;qty=q;} }
    List<Resting> asks=new ArrayList<>(), bids=new ArrayList<>();
    long seq=0;
    long nextSeq(){ return ++seq; }
    public void cancel(String orderId){}                       // BUG
    public List<Trade> limit(String orderId, String side, long price, long qty){
        List<Trade> trades=new ArrayList<>();
        if(side.equals("buy")){
            asks.sort((a,b)-> a.price!=b.price ? Long.compare(a.price,b.price) : Long.compare(b.seq,a.seq)); // BUG -seq
            int i=0;
            while(qty>0 && i<asks.size()){
                Resting r=asks.get(i);
                if(r.price<=price){ long fill=Math.min(qty,r.qty); trades.add(new Trade(r.orderId,orderId,r.price,fill)); qty-=fill; asks.remove(i); } // BUG remove whole
                else break;
            }
            if(qty>0) bids.add(new Resting(orderId,"buy",price,qty,nextSeq()));
        } else {
            bids.sort((a,b)-> a.price!=b.price ? Long.compare(b.price,a.price) : Long.compare(b.seq,a.seq));
            int i=0;
            while(qty>0 && i<bids.size()){
                Resting r=bids.get(i);
                if(r.price>=price){ long fill=Math.min(qty,r.qty); trades.add(new Trade(r.orderId,orderId,r.price,fill)); qty-=fill; bids.remove(i); }
                else break;
            }
            if(qty>0) asks.add(new Resting(orderId,"sell",price,qty,nextSeq()));
        }
        return trades;
    }
}
