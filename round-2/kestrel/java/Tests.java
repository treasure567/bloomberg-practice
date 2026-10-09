import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Matching b=new Matching(); b.limit("A","sell",100,5); b.limit("B","sell",100,5); List<Matching.Trade> t=b.limit("T","buy",100,5);
          check("price_time_priority_fifo", t.size()==1 && t.get(0).makerId.equals("A")); }
        { Matching b=new Matching(); b.limit("A","sell",100,10); List<Matching.Trade> f=b.limit("T1","buy",100,4); List<Matching.Trade> s=b.limit("T2","buy",100,6);
          check("partial_fill_reduces_resting_qty", f.size()==1 && f.get(0).qty==4 && s.size()==1 && s.get(0).qty==6); }
        { Matching b=new Matching(); b.limit("A","sell",100,5); b.cancel("A"); List<Matching.Trade> t=b.limit("T","buy",100,5);
          check("cancel_removes_resting_order", t.isEmpty()); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
