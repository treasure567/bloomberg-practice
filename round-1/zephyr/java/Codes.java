public class Codes {
    public static final String PREFIX = "ORD";

    public static int checkDigit(String body) {
        int s = 0;
        for (char c : body.toCharArray()) s += (c - '0');
        return s % 10;
    }

    public static String formatCode(int seq) {
        String body = Integer.toString(seq);
        return PREFIX + "-" + body + "-" + checkDigit(body);
    }

    public static boolean isValid(String code) {
        return code.startsWith(PREFIX + "-");
    }
}
