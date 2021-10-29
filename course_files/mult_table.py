def multi(x1, x2):
    """
    Print Multi table.

    :param x1: First multiplier
    :type x1: int
    :param x2: Second multiplier
    :type x2: int
    """
    for i in range(1, x2+1):
        for j in range(1, x1+1):
            print(f"{j} x {i} = {i * j}", end='\t')
        print()


multi(5, 9)
