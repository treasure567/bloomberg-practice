import java.util.*;
import java.util.function.BiFunction;

public class Payouts {
    public static final long POT_SEED_CENTS = 1000000, ENTRY_FEE_CENTS = 500;

    public static class Payout {
        public final String participant; public final int matchCount; public final long amountCents;
        public Payout(String p, int m, long a) { participant = p; matchCount = m; amountCents = a; }
    }
    public static class DrawResult {
        public final long potCents; public final List<Payout> payouts; public final long rolloverCents;
        public DrawResult(long p, List<Payout> ps, long r) { potCents = p; payouts = ps; rolloverCents = r; }
    }

    public static long potCents(int entryCount) { return POT_SEED_CENTS + ENTRY_FEE_CENTS * entryCount; }

    public static DrawResult distribute(List<Codes.Entry> entries, String winning,
                                        BiFunction<String, String, Integer> matcher) {
        long pot = potCents(entries.size());
        Map<Integer, List<Codes.Entry>> byTier = new HashMap<>();
        for (Codes.Entry e : entries) {
            int m = matcher.apply(e.code, winning);
            if (m >= 2) byTier.computeIfAbsent(m, k -> new ArrayList<>()).add(e);
        }
        Map<Integer, Integer> tierPercent = Map.of(5, 100, 4, 40, 3, 20, 2, 5);
        List<Payout> payouts = new ArrayList<>();
        long awarded = 0;
        for (int tier : new int[]{2, 3, 4, 5}) {
            List<Codes.Entry> ws = byTier.get(tier);
            if (ws == null) continue;
            long amount = pot * tierPercent.get(tier) / 100;
            double share = (double) amount / ws.size();
            for (Codes.Entry w : ws) {
                payouts.add(new Payout(w.participant, tier, (long) share));
                awarded += (long) share;
            }
        }
        return new DrawResult(pot, payouts, pot - awarded);
    }
}
