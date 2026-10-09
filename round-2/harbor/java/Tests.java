import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    static void checkThrows(String n, Runnable r){ total++; boolean t=false; try{r.run();}catch(RuntimeException e){t=true;} if(t) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    static Payments svc(){ Payments s=new Payments(); s.openAccount("A"); s.openAccount("B"); return s; }
    public static void main(String[] a){
        { Payments s=svc(); s.deposit("A",100); s.transfer("t1","A","B",40); check("transfer_moves_funds", s.balance("A")==60 && s.balance("B")==40); }
        { Payments s=svc(); s.deposit("A",100); s.transfer("t1","A","B",40); s.transfer("t1","A","B",40); check("transfer_is_idempotent", s.balance("B")==40); }
        { Payments s=svc(); s.deposit("A",100); s.placeHold("h1","A",40); checkThrows("overdraft_rejected", ()-> s.transfer("t1","A","B",80)); }
        { Payments s=svc(); s.deposit("A",100); s.placeHold("h1","A",30); boolean x=s.available("A")==70; s.releaseHold("h1"); check("release_restores_available", x && s.available("A")==100); }
        { Payments s=svc(); s.deposit("A",100); s.transfer("t1","A","B",40); long sum=0; for(long v:s.balances().values()) sum+=v; check("double_entry_conservation", sum==0); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
