# tests/test_mymath.py
from mymath.mymath import add

def test_add():
    assert add(2, 3) == 5
    assert add(0,0) == 0