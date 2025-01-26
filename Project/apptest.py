from app import add
def test_add_positive_number():
    result = add(2, 3)
    assert result == 8

def test_add_negative_number():
    result = add(-2, -3)
    assert result == -5