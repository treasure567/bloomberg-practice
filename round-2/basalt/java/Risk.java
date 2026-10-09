import java.util.*;
public class Risk {
    Map<String,Long> net=new HashMap<>();
    Set<String> seen=new HashSet<>();
    String key(String cp,String symbol){ return symbol; }
    public void addTrade(String tradeId,String cp,String symbol,long qty){ net.merge(key(cp,symbol), Math.abs(qty), Long::sum); }
    public long netPosition(String cp,String symbol){ return net.getOrDefault(key(cp,symbol),0L); }
}
