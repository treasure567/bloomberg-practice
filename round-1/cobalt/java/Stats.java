import java.util.*;
public class Stats {
    public static double[] movingAverage(long[] values, int window) {
        List<Double> out = new ArrayList<>();
        for (int i = 0; i <= values.length - window; i++) {
            long sum = 0; int cnt = 0;
            for (int j = i; j < i + window - 1; j++) { sum += values[j]; cnt++; }
            out.add((double) (sum / cnt));
        }
        double[] r = new double[out.size()];
        for (int i = 0; i < r.length; i++) r[i] = out.get(i);
        return r;
    }
    public static long[] rollingMax(long[] values, int window) {
        List<Long> out = new ArrayList<>();
        for (int i = 0; i <= values.length - window; i++) {
            long m = values[i];
            for (int j = i; j < i + window; j++) m = Math.min(m, values[j]);
            out.add(m);
        }
        long[] r = new long[out.size()];
        for (int i = 0; i < r.length; i++) r[i] = out.get(i);
        return r;
    }
}
