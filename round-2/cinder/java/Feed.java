import java.util.*;
import java.util.function.Consumer;
public class Feed {
    public static class Quote { public String symbol; public long bid, ask, seq; public Quote(String s,long b,long a,long q){symbol=s;bid=b;ask=a;seq=q;} }
    public static class QuoteStore {
        Map<String,Quote> quotes = new HashMap<>();
        public void apply(Quote q){ quotes.put(q.symbol, q); }                 // BUG no seq guard
        public Quote get(String s){ return quotes.get(s); }
    }
    public static class SubscriptionHub {
        static class Sub { int token; Consumer<Quote> cb; Sub(int t,Consumer<Quote> c){token=t;cb=c;} }
        Map<String,List<Sub>> subs = new HashMap<>();
        int counter = 0;
        public int subscribe(String sym, Consumer<Quote> cb){ int t=++counter; subs.computeIfAbsent(sym,k->new ArrayList<>()).add(new Sub(t,cb)); return t; }
        public void unsubscribe(String sym, int token){
            List<Sub> keep = new ArrayList<>();
            for(Sub s: subs.getOrDefault(sym, new ArrayList<>())) if(s.token==token) keep.add(s);  // BUG inverted
            subs.put(sym, keep);
        }
        public void publish(String sym, Quote q){
            for(Sub s: subs.getOrDefault(sym, new ArrayList<>())) s.cb.accept(q);                   // BUG no isolation
        }
    }
    public static class MarketDataFeed {
        QuoteStore store;
        public MarketDataFeed(QuoteStore s){ store=s; }
        public void applySnapshot(Quote q){ store.apply(q); }
        public void applyDelta(String sym, long seq, long bid, long ask){
            Quote cur = store.get(sym);
            long b = cur!=null ? cur.bid : 0;                                  // BUG fabricates base
            long a = cur!=null ? cur.ask : 0;
            store.apply(new Quote(sym, bid!=0?bid:b, ask!=0?ask:a, seq));
        }
    }
}
