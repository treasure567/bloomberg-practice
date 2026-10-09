public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    static void checkThrows(String n, Runnable r){ total++; boolean t=false; try{r.run();}catch(RuntimeException e){t=true;} if(t) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    static Fulfillment svc(){ Fulfillment s=new Fulfillment(); s.addSku("A"); s.setStock("A",10); return s; }
    public static void main(String[] a){
        { Fulfillment s=svc(); s.reserve("r1","A",3); check("available_reflects_reservations", s.available("A")==7); }
        { Fulfillment s=svc(); checkThrows("oversell_rejected", ()-> s.reserve("r2","A",100)); }
        { Fulfillment s=svc(); s.reserve("r1","A",3); boolean x=s.available("A")==7; s.release("r1"); check("release_restores_availability", x && s.reserved("A")==0 && s.available("A")==10); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
