import java.util.*;
public class Cache {
    private final int capacity;
    private final LinkedHashMap<String,Long> data = new LinkedHashMap<>();
    public Cache(int capacity){ this.capacity = capacity; }
    public Long get(String k){ return data.get(k); }          // BUG: no recency refresh
    public void put(String k, long v){
        data.put(k, v);                                       // BUG: update does not move to most-recent
        if (data.size() > capacity) {
            String last = null;
            for (String key : data.keySet()) last = key;      // most-recently inserted
            data.remove(last);                                // BUG: evicts most-recent instead of LRU
        }
    }
}
