public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        check("rounds_up_near_tick", Tick.roundToTick(103,5)==105);
        check("rounds_to_nearest", Tick.roundToTick(108,5)==110);
        check("tie_rounds_up", Tick.roundToTick(1025,50)==1050);
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
