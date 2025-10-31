from task2.interpreter import evaluate

def test_add_sub_mul_div():
    assert evaluate("2+3-1") == 4
    assert evaluate("2*3") == 6
    assert evaluate("8/2") == 4

def test_precedence():
    assert evaluate("2+3*4") == 14
    assert evaluate("2*3+4") == 10
