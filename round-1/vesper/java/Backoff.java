public class Backoff {
    public static long[] backoffDelays(long base, int attempts, long maxDelay) {
        long[] out = new long[attempts];
        for (int a = 1; a <= attempts; a++) out[a - 1] = base * (1L << a);
        return out;
    }
}
