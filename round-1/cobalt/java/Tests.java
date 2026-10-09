import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        check("moving_average_basic", Arrays.equals(Stats.movingAverage(new long[]{1,2,3,4},2), new double[]{1.5,2.5,3.5}));
        check("moving_average_full_window", Arrays.equals(Stats.movingAverage(new long[]{2,4,6},3), new double[]{4.0}));
        check("rolling_max", Arrays.equals(Stats.rollingMax(new long[]{1,3,2,5,4},2), new long[]{3,3,5,5}));
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
