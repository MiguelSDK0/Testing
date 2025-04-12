from primos2 import *

def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(49) == True # 49 no es primo pero da un resultado como si fuera primo
    assert isPrime2(49) == False # en la función isPrime2 se solucionó este error, por ende el resultado es FALSE
    assert isPrime(121) == True # 121 tampoco es un número primo, pero la función isPrime da como verdadera la respuesta
    assert isPrime2(121) == False # 121 en la funsión isPrime2 si da como respuesta FALSE