import java.util.*;
public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    static boolean eq(int[][] a, int[][] b){ return Arrays.deepEquals(a,b); }
    public static void main(String[] a){
        check("merge_unsorted_overlaps", eq(Intervals.merge(new int[][]{{1,3},{2,4},{8,10},{4,6}}), new int[][]{{1,6},{8,10}}));
        check("touching_intervals_merge", eq(Intervals.merge(new int[][]{{1,2},{2,3}}), new int[][]{{1,3}}));
        check("output_sorted", eq(Intervals.merge(new int[][]{{5,6},{1,2}}), new int[][]{{1,2},{5,6}}));
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
