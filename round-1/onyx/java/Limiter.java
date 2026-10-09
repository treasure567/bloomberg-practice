public class Limiter {
    private final long limit, window;
    private long cur = -1, count = 0;
    public Limiter(long limit, long window) { this.limit = limit; this.window = window; }
    public boolean allow(long now) {
        long w = now / window;
        if (w != cur) { cur = w; count = 0; }
        if (count <= limit) { count++; return true; }
        return false;
    }
}
