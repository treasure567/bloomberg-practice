public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Risk s=new Risk(); s.addTrade("t1","cpA","X",10); s.addTrade("t2","cpA","X",-4); check("signed_netting", s.netPosition("cpA","X")==6); }
        { Risk s=new Risk(); s.addTrade("t1","cpA","X",10); s.addTrade("t1","cpA","X",10); check("idempotent_on_trade_id", s.netPosition("cpA","X")==10); }
        { Risk s=new Risk(); s.addTrade("t1","cpA","X",10); s.addTrade("t2","cpB","X",5); check("counterparties_isolated", s.netPosition("cpA","X")==10 && s.netPosition("cpB","X")==5); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
