import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        check("split_100_3", Arrays.equals(Split.splitAmount(100,3), new long[]{34,33,33}));
        check("split_10_4", Arrays.equals(Split.splitAmount(10,4), new long[]{3,3,2,2}));
        check("split_7_2", Arrays.equals(Split.splitAmount(7,2), new long[]{4,3}));
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
