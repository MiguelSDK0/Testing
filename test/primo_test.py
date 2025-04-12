from primos import esprimo

def test_1():
    resultado = esprimo(1)
    assert resultado == False

def test_2():
    resultado = esprimo(3)
    assert resultado == True

def test_3():
    resultado = esprimo(5)
    assert resultado == True

def test_4():
    resultado = esprimo(10)
    assert resultado == False

def test_5():
    resultado = esprimo(12)
    assert resultado == False

def test_6():
    resultado = esprimo(15)
    assert resultado == False

def test_7():
    resultado = esprimo(17)
    assert resultado == True

def test_8():
    resultado = esprimo(23)
    assert resultado == True

def test_9():
    resultado = esprimo(33)
    assert resultado == False

def test_10():
    resultado = esprimo(20)
    assert resultado == False

def test_11():
    resultado = esprimo(18)
    assert resultado == False

def test_12():
    resultado = esprimo(34)
    assert resultado == False

def test_13():
    resultado = esprimo(21)
    assert resultado == False

def test_14():
    resultado = esprimo(86)
    assert resultado == False

def test_15():
    resultado = esprimo(120)
    assert resultado == False