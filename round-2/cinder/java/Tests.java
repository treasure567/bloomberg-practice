import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Feed.QuoteStore s=new Feed.QuoteStore(); s.apply(new Feed.Quote("AAPL",110,111,2)); s.apply(new Feed.Quote("AAPL",100,101,1));
          Feed.Quote q=s.get("AAPL"); check("store_ignores_stale_seq", q!=null && q.seq==2 && q.bid==110); }
        { Feed.SubscriptionHub h=new Feed.SubscriptionHub(); int[] got={0}; int t=h.subscribe("AAPL", q->got[0]++); h.unsubscribe("AAPL",t);
          h.publish("AAPL", new Feed.Quote("AAPL",100,101,1)); check("unsubscribe_stops_callbacks", got[0]==0); }
        { Feed.SubscriptionHub h=new Feed.SubscriptionHub(); List<Long> got=new ArrayList<>();
          h.subscribe("AAPL", q->{ throw new RuntimeException("boom"); });
          h.subscribe("AAPL", q->got.add(q.bid));
          try { h.publish("AAPL", new Feed.Quote("AAPL",100,101,1)); } catch(Exception e){}
          check("publish_isolates_subscriber_errors", got.size()==1 && got.get(0)==100); }
        { Feed.QuoteStore s=new Feed.QuoteStore(); Feed.MarketDataFeed f=new Feed.MarketDataFeed(s); boolean raised=false;
          try { f.applyDelta("AAPL",1,100,101); } catch(RuntimeException e){ raised=true; }
          check("delta_before_snapshot_raises", raised); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
