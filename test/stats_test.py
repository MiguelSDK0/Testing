from stats import *

def test1():
    assert stats([1, 2, 3]) == {
        "list": [1, 2, 3],
        "min": 1,
        "max": 3,
        "median": 2,
        "mode": [1, 2, 3]
    }

def test2():
    assert stats([1, 2, 3, 4]) == {
        "list": [1, 2, 3, 4],
        "min": 1,
        "max": 4,
        "median": 2.5,
        "mode": [1, 2, 3, 4]
    }

def test3():
    assert stats([4, 1, 2, 1, 2, 3, 4]) == {
        "list": [4, 1, 2, 1, 2, 3, 4],
        "min": 1,
        "max": 4,
        "median": 2,
        "mode": [1, 2, 4]
    }