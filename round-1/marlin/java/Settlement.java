import java.util.*;

public class Settlement {
    public static class Position { public long quantity, costBasisCents, lastPriceCents; }
    public static class Fill {
        public final String tradeId, symbol, side; public final long quantity, priceCents;
        public Fill(String t, String s, String side, long q, long p) { tradeId = t; symbol = s; this.side = side; quantity = q; priceCents = p; }
    }

    public final Map<String, Position> positions = new HashMap<>();
    public long realizedPnlCents = 0;
    public final Set<String> seen = new HashSet<>();

    public void apply(Fill f) {
        Position pos = positions.computeIfAbsent(f.symbol, k -> new Position());
        if (f.side.equals("buy")) {
            pos.quantity += f.quantity;
            pos.costBasisCents += f.quantity * f.priceCents;
            pos.lastPriceCents = f.priceCents;
        } else {
            double avg = (double) pos.costBasisCents / pos.quantity;
            realizedPnlCents += (f.priceCents - pos.lastPriceCents) * f.quantity;
            pos.quantity -= f.quantity;
            pos.costBasisCents -= (long) (avg * f.quantity);
        }
    }

    public static Settlement settle(List<Fill> fills) {
        Settlement b = new Settlement();
        for (Fill f : fills) b.apply(f);
        return b;
    }
}
