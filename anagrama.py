def es_anagrama(p1, p2):
    p1 = p1.replace(" ", "").lower()
    p2 = p2.replace(" ", "").lower()

    if sorted(p1) == sorted(p2):
        return True
    else:
        return False