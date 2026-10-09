from codes import CodeIssuer
from payouts import distribute


def issuer(r):
    return CodeIssuer(random_source=lambda: r)


def test_code_zero_is_five_zeros():
    assert issuer(0.0).issue("Mina").code == "00000"


def test_code_preserves_leading_zeros():
    assert issuer(0.00042).issue("Mina").code == "00042"


def test_match_is_positional():
    e = CodeIssuer().issue.__self__  # noqa
    from codes import Entry
    entries = [Entry("Ada", "54321")]
    res = distribute(entries, "12345", CodeIssuer.match_count)
    assert all(p.participant != "Ada" for p in res.payouts)


def test_five_match_consumes_pot():
    from codes import Entry
    entries = [Entry("Win", "12345"), Entry("Two", "12000")]
    res = distribute(entries, "12345", CodeIssuer.match_count)
    paid = {p.participant: p.amount_cents for p in res.payouts}
    assert paid.get("Win") == res.pot_cents
    assert "Two" not in paid


def test_tier_split_conserves_cents():
    from codes import Entry
    entries = [Entry(n, "12000") for n in ("X", "Y", "Z")]
    res = distribute(entries, "12999", CodeIssuer.match_count)
    total = sum(p.amount_cents for p in res.payouts if p.match_count == 2)
    assert total == res.pot_cents * 5 // 100
