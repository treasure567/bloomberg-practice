import java.util.*;
public class Intervals {
    public static int[][] merge(int[][] intervals) {
        if (intervals.length == 0) return new int[0][];
        List<int[]> merged = new ArrayList<>();
        merged.add(new int[]{intervals[0][0], intervals[0][1]});
        for (int i = 1; i < intervals.length; i++) {
            int[] iv = intervals[i], last = merged.get(merged.size() - 1);
            if (iv[0] < last[1]) last[1] = Math.max(last[1], iv[1]);
            else merged.add(new int[]{iv[0], iv[1]});
        }
        return merged.toArray(new int[0][]);
    }
}
