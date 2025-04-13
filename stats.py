def stats(lst):
    min_val = None
    max_val = None
    freq = {}

    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        freq[i] = freq.get(i, 0) + 1

    lst_sorted = sorted(lst)
    middle = len(lst_sorted) // 2 # Los indices de las islas deben de estar en enteros, /2 daba un número decimal, por eso se cambio a //2 para mostrar un número entero
    if len(lst_sorted) % 2 == 0:
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        median = lst_sorted[middle]

    mode_times = max(freq.values())
    mode = [num for num, count in freq.items() if count == mode_times]

    return {
        "list": lst,
        "min": min_val,
        "max": max_val,
        "median": median,
        "mode": sorted(mode)
    }