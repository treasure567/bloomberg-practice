import java.util.*;
import java.util.function.Consumer;
public class Bus {
    static class Sub { int token; String pattern; Consumer<String> cb; Sub(int t,String p,Consumer<String> c){token=t;pattern=p;cb=c;} }
    List<Sub> subs=new ArrayList<>(); int counter=0;
    public int subscribe(String pattern, Consumer<String> cb){ int t=++counter; subs.add(new Sub(t,pattern,cb)); return t; }
    public void unsubscribe(int token){ List<Sub> keep=new ArrayList<>(); for(Sub s:subs) if(!s.pattern.equals(String.valueOf(token))) keep.add(s); subs=keep; } // BUG
    boolean matches(String pattern,String topic){ return pattern.equals(topic); } // BUG no wildcard
    public void publish(String topic,String msg){ for(Sub s:subs) if(matches(s.pattern,topic)) s.cb.accept(msg); } // BUG no isolation
}
