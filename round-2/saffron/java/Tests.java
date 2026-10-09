public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Sessions s=new Sessions(); s.create("s",0,10); check("expiry_boundary_is_inclusive", !s.valid("s",10)); }
        { Sessions s=new Sessions(); s.create("s",0,10); s.touch("s",8,10); check("touch_refreshes_expiry", s.valid("s",15)); }
        { Sessions s=new Sessions(); s.create("s",0,10); s.cleanup(10); check("cleanup_removes_expired", !s.valid("s",10) && s.size()==0); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
