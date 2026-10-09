public class Tick {
    public static long roundToTick(long priceCents, long tickCents) {
        return (priceCents / tickCents) * tickCents;
    }
}
