# for running using doctest
# $ python3 -m doctest -v course_files/doctest.py
def product(el1, el2):
    """
    multiply two parameters

    >>> product(2,2)
    4

    >>> product(2,-2)
    -4

    >>> product(3, None)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return el1 * el2


print(product(3, 2))
