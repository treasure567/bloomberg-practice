import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        check("exponential_growth", Arrays.equals(Backoff.backoffDelays(1,4,100), new long[]{1,2,4,8}));
        check("capped_at_max", Arrays.equals(Backoff.backoffDelays(1,5,5), new long[]{1,2,4,5,5}));
        check("nonunit_base", Arrays.equals(Backoff.backoffDelays(3,3,100), new long[]{3,6,12}));
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
