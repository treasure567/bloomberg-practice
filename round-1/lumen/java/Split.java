public class Split {
    public static long[] splitAmount(long totalCents, int n) {
        long each = (long) ((double) totalCents / n);
        long[] out = new long[n];
        for (int i = 0; i < n; i++) out[i] = each;
        return out;
    }
}
