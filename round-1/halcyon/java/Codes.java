import java.util.*;
import java.util.function.Supplier;

public class Codes {
    public static class Entry {
        public final String participant, code;
        public Entry(String p, String c) { participant = p; code = c; }
    }

    private final Supplier<Double> randSource;
    public Codes(Supplier<Double> r) { randSource = r; }

    public Entry issue(String participant) {
        int number = (int) (randSource.get() * 100000);
        return new Entry(participant, Integer.toString(number));
    }

    public static int matchCount(String code, String winning) {
        Set<Character> a = new HashSet<>(), b = new HashSet<>();
        for (char c : code.toCharArray()) a.add(c);
        for (char c : winning.toCharArray()) b.add(c);
        int n = 0;
        for (char c : a) if (b.contains(c)) n++;
        return n;
    }
}
