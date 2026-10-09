from orchestration.service import OrchestrationService


def test_dequeue_removes_job():
    s = OrchestrationService()
    s.enqueue("A")
    assert s.dequeue() == "A"
    assert s.dequeue() is None


def test_ack_completes_job():
    s = OrchestrationService()
    s.enqueue("A")
    jid = s.dequeue()
    s.ack(jid)
    assert s.dequeue() is None


def test_two_nacks_dead_letter_at_max_2():
    s = OrchestrationService(max_retries=2)
    s.enqueue("A")
    s.nack("A")
    s.nack("A")
    assert "A" in s.dead_letters()


def test_one_nack_dead_letter_at_max_1():
    s = OrchestrationService(max_retries=1)
    s.enqueue("A")
    s.nack("A")
    assert "A" in s.dead_letters()
