import java.util.*;

public class Tests {
    static int total = 0, failures = 0;
    static void check(String n, boolean c) { total++; if (c) System.out.println("PASS " + n); else { failures++; System.out.println("FAIL " + n); } }
    static void checkThrows(String n, Runnable r) {
        total++; boolean threw = false;
        try { r.run(); } catch (RuntimeException e) { threw = true; }
        if (threw) System.out.println("PASS " + n); else { failures++; System.out.println("FAIL " + n); }
    }
    static Settlement.Fill buy(String t, String s, long q, long p) { return new Settlement.Fill(t, s, "buy", q, p); }
    static Settlement.Fill sell(String t, String s, long q, long p) { return new Settlement.Fill(t, s, "sell", q, p); }

    public static void main(String[] a) {
        {
            Settlement b = Settlement.settle(List.of(buy("1", "AAPL", 10, 10000), buy("1", "AAPL", 10, 10000)));
            check("duplicate_trade_id_applied_once", b.positions.get("AAPL").quantity == 10);
        }
        {
            Settlement b = Settlement.settle(List.of(buy("1", "AAPL", 10, 10000), buy("2", "AAPL", 10, 20000), sell("3", "AAPL", 10, 18000)));
            check("realized_pnl_uses_average_cost", b.realizedPnlCents == 30000);
        }
        checkThrows("oversell_raises", () -> { new Settlement().apply(sell("1", "AAPL", 5, 10000)); });
        checkThrows("malformed_fill_raises", () -> { new Settlement().apply(buy("1", "A", 0, 100)); });

        System.out.println((failures > 0 ? "FAILED " : "OK ") + (total - failures) + "/" + total);
        System.exit(failures > 0 ? 1 : 0);
    }
}
