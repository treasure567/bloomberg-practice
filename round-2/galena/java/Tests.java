import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Bus b=new Bus(); List<String> got=new ArrayList<>(); b.subscribe("px.*", got::add); b.publish("px.AAPL","hi");
          check("wildcard_segment_match", got.size()==1 && got.get(0).equals("hi")); }
        { Bus b=new Bus(); List<String> got=new ArrayList<>(); int t=b.subscribe("px.AAPL", got::add); b.unsubscribe(t); b.publish("px.AAPL","hi");
          check("unsubscribe_stops_delivery", got.isEmpty()); }
        { Bus b=new Bus(); List<String> got=new ArrayList<>();
          b.subscribe("px.AAPL", m -> { throw new RuntimeException("boom"); });
          b.subscribe("px.AAPL", got::add);
          try { b.publish("px.AAPL","hi"); } catch(RuntimeException e) {}
          check("raising_subscriber_does_not_block_others", got.size()==1 && got.get(0).equals("hi")); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
