public class Tests {
    static int total=0, failures=0;
    static void check(String n, boolean c){ total++; if(c) System.out.println("PASS "+n); else { failures++; System.out.println("FAIL "+n);} }
    public static void main(String[] a){
        { Orchestration s=new Orchestration(3); s.enqueue("A"); String x=s.dequeue(); check("dequeue_removes_job", "A".equals(x) && s.dequeue()==null); }
        { Orchestration s=new Orchestration(3); s.enqueue("A"); String j=s.dequeue(); s.ack(j); check("ack_completes_job", s.dequeue()==null); }
        { Orchestration s=new Orchestration(2); s.enqueue("A"); s.nack("A"); s.nack("A"); check("two_nacks_dead_letter_at_max_2", s.deadLetters().contains("A")); }
        { Orchestration s=new Orchestration(1); s.enqueue("A"); s.nack("A"); check("one_nack_dead_letter_at_max_1", s.deadLetters().contains("A")); }
        System.out.println((failures>0?"FAILED ":"OK ")+(total-failures)+"/"+total); System.exit(failures>0?1:0);
    }
}
