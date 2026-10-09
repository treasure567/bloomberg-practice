from codes import format_code, is_valid


def test_format_pads_and_checks():
    assert format_code(42) == "ORD-00000042-6"


def test_format_zero():
    assert format_code(0) == "ORD-00000000-0"


def test_valid_true_and_false_on_checkdigit():
    assert is_valid("ORD-00000042-6") is True
    assert is_valid("ORD-00000042-7") is False


def test_invalid_when_missing_check_segment():
    assert is_valid("ORD-00000042") is False
