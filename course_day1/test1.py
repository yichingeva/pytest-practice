import pytest
from module1 import add, subtract, multiply, divide

def test_add():
    assert add(3, 6) == 9
    assert add(-3, 5) == 2
def test_subtract():
    assert subtract(9, 6) == 3
    assert subtract(-4, 10) == -14
def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(5, 2) == 10
def test_divide():
    assert divide(8, 2) == 4
    assert divide(15, 3) == 5

if __name__ == '__main__':
    pytest.main(['-v', 'test1.py'])