public class Fees {
    public static final long MIN_FEE_CENTS = 50;
    public static double rateFor(long amountCents) {
        if (amountCents <= 10000) return 0.02;
        if (amountCents <= 100000) return 0.01;
        return 0.005;
    }
    public static long feeFor(long amountCents) {
        return (long) (amountCents * rateFor(amountCents));
    }
}
