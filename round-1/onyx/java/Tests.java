public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Limiter l=new Limiter(2,10); check("blocks_after_limit", l.allow(0)&&l.allow(1)&&!l.allow(2)); }
        { Limiter l=new Limiter(2,10); boolean x=l.allow(0),y=l.allow(1),z=l.allow(2),w=l.allow(10);
          check("resets_next_window", x&&y&&!z&&w); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
