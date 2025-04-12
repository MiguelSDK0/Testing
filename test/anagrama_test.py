from anagrama import es_anagrama

def test_1():
    resultado = es_anagrama("Copo", "Poco")
    assert resultado == True

def test_2():
    resultado = es_anagrama("amor", "roma")
    assert resultado == True

def test_3():
    resultado = es_anagrama("Capa", "Mapa")
    assert resultado == False

def test_4():
    resultado = es_anagrama("Cara", "Arca")
    assert resultado == True

def test_5():
    resultado = es_anagrama("Queso", "Hueso")
    assert resultado == False

def test_6():
    resultado = es_anagrama("Castor", "Castro")
    assert resultado == True

def test_7():
    resultado = es_anagrama("Genio", "Niego")
    assert resultado == True

def test_8():
    resultado = es_anagrama("Raton", "Tazon")
    assert resultado == False

def test_9():
    resultado = es_anagrama("Taco", "Capo")
    assert resultado == False

def test_10():
    resultado = es_anagrama("Las", "Sal")
    assert resultado == True

def test_11():
    resultado = es_anagrama("Directo", "Credito")
    assert resultado == True

def test_12():
    resultado = es_anagrama("Salir", "Partir")
    assert resultado == False

def test_13():
    resultado = es_anagrama("Raton", "Tazon")
    assert resultado == False

def test_14():
    resultado = es_anagrama("Sol", "Los")
    assert resultado == True

def test_15():
    resultado = es_anagrama("Casa", "Cama")
    assert resultado == False