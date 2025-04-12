from palindromo_capicua import palindromo_o_capicua

def test_1():
    resultado = palindromo_o_capicua("Hola")
    assert resultado == False

def test_2():
    resultado = palindromo_o_capicua(123)
    assert resultado == False

def test_3():
    resultado = palindromo_o_capicua("Oso")
    assert resultado == True

def test_4():
    resultado = palindromo_o_capicua(123321)
    assert resultado == True


def test_5():
    resultado = palindromo_o_capicua("Casa")
    assert resultado == False

def test_6():
    resultado = palindromo_o_capicua("Anilina")
    assert resultado == True

def test_7():
    resultado = palindromo_o_capicua("Fruta")
    assert resultado == False

def test_8():
    resultado = palindromo_o_capicua(10001)
    assert resultado == True


def test_9():
    resultado = palindromo_o_capicua("Radar")
    assert resultado == True

def test_10():
    resultado = palindromo_o_capicua(2025)
    assert resultado == False

def test_11():
    resultado = palindromo_o_capicua("Reconocer")
    assert resultado == True

def test_12():
    resultado = palindromo_o_capicua("Jaja")
    assert resultado == False

def test_13():
    resultado = palindromo_o_capicua("Oro")
    assert resultado == True

def test_14():
    resultado = palindromo_o_capicua("Radar")
    assert resultado == True

def test_15():
    resultado = palindromo_o_capicua(1009)
    assert resultado == False