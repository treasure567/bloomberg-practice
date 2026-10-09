public class Tests {
    static int total = 0, failures = 0;
    static void check(String n, boolean c) { total++; if (c) System.out.println("PASS " + n); else { failures++; System.out.println("FAIL " + n); } }

    public static void main(String[] a) {
        check("format_pads_and_checks", Codes.formatCode(42).equals("ORD-00000042-6"));
        check("format_zero", Codes.formatCode(0).equals("ORD-00000000-0"));
        check("valid_true_and_false_on_checkdigit", Codes.isValid("ORD-00000042-6") && !Codes.isValid("ORD-00000042-7"));
        check("invalid_when_missing_check_segment", !Codes.isValid("ORD-00000042"));
        System.out.println((failures > 0 ? "FAILED " : "OK ") + (total - failures) + "/" + total);
        System.exit(failures > 0 ? 1 : 0);
    }
}
