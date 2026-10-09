import java.util.*;

public class Tests {
    static int total = 0, failures = 0;
    static void check(String name, boolean cond) {
        total++;
        if (cond) System.out.println("PASS " + name);
        else { failures++; System.out.println("FAIL " + name); }
    }

    public static void main(String[] args) {
        check("code_zero_is_five_zeros", new Codes(() -> 0.0).issue("Mina").code.equals("00000"));
        check("code_preserves_leading_zeros", new Codes(() -> 0.00042).issue("Mina").code.equals("00042"));

        {
            List<Codes.Entry> e = List.of(new Codes.Entry("Ada", "54321"));
            Payouts.DrawResult r = Payouts.distribute(e, "12345", Codes::matchCount);
            boolean ada = false;
            for (Payouts.Payout p : r.payouts) if (p.participant.equals("Ada")) ada = true;
            check("match_is_positional", !ada);
        }
        {
            List<Codes.Entry> e = List.of(new Codes.Entry("Win", "12345"), new Codes.Entry("Two", "12000"));
            Payouts.DrawResult r = Payouts.distribute(e, "12345", Codes::matchCount);
            long win = -1; boolean two = false;
            for (Payouts.Payout p : r.payouts) { if (p.participant.equals("Win")) win = p.amountCents; if (p.participant.equals("Two")) two = true; }
            check("five_match_consumes_pot", win == r.potCents && !two);
        }
        {
            List<Codes.Entry> e = List.of(new Codes.Entry("X", "12000"), new Codes.Entry("Y", "12000"), new Codes.Entry("Z", "12000"));
            Payouts.DrawResult r = Payouts.distribute(e, "12999", Codes::matchCount);
            long t2 = 0;
            for (Payouts.Payout p : r.payouts) if (p.matchCount == 2) t2 += p.amountCents;
            check("tier_split_conserves_cents", t2 == r.potCents * 5 / 100);
        }

        System.out.println((failures > 0 ? "FAILED " : "OK ") + (total - failures) + "/" + total);
        System.exit(failures > 0 ? 1 : 0);
    }
}
