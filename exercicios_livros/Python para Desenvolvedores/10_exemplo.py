def fib(n):

    if not type(n) is int:
        raise TypeError
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1
    
def _doctest():
    """
    Evoca o doctest.
    """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()