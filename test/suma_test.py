from suma import *
def test1():
    assert add8(0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0) == (0,0,0,0,0,0,0,0,0)

def test2():
    assert add8(1,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0, 0) == (0,1,0,0,0,0,0,0,0)

def test3():
    assert add8(1,0,0,0,0,0,0,0, 1,0,0,0,0,0,0,0, 1) == (1,1,0,0,0,0,0,0,0)

def test4():
    assert add8(1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0, 0) == (0,0,0,0,0,0,0,0,1)