public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        check("min_fee_floor", Fees.feeFor(2000)==50);
        check("boundary_10000_is_one_percent", Fees.feeFor(10000)==100);
        check("boundary_100000_is_half_percent", Fees.feeFor(100000)==500);
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
