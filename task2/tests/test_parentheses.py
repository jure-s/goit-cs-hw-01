from task2.interpreter import evaluate

def test_parentheses():
    assert evaluate("(2+3)*4") == 20
    assert evaluate("2*(3+4)") == 14
    assert evaluate("(1+(2*3)-4)/2") == 1.5

def test_unary():
    assert evaluate("-3+5") == 2
    assert evaluate("+7") == 7
    assert evaluate("-(2+3)*2") == -10
