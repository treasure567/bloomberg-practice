public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    static boolean isNull(Long v){ return v == null; }
    public static void main(String[] a){
        { Cache c=new Cache(2); c.put("a",1); c.put("b",2); c.put("c",3);
          check("evicts_least_recently_used", isNull(c.get("a")) && c.get("b")!=null && c.get("b")==2 && c.get("c")!=null && c.get("c")==3); }
        { Cache c=new Cache(2); c.put("a",1); c.put("b",2); c.get("a"); c.put("c",3);
          check("get_refreshes_recency", c.get("a")!=null && c.get("a")==1 && isNull(c.get("b"))); }
        { Cache c=new Cache(2); c.put("a",1); c.put("b",2); c.put("a",9); c.put("c",3);
          check("update_existing_refreshes_without_growth", c.get("a")!=null && c.get("a")==9 && isNull(c.get("b"))); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
