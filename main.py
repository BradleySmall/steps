def NFact135():
    def fact(x):
        _fact = 1
        for i in range(1, x + 1):
            _fact = _fact * i
        return _fact

    #        Leaps         Ones      threes    fives
    return (
        fact(10) // (fact(10) * fact(0) * fact(0))
        + fact(8) // (fact(7) * fact(1) * fact(0))
        + fact(6) // (fact(4) * fact(2) * fact(0))
        + fact(6) // (fact(5) * fact(0) * fact(1))
        + fact(4) // (fact(1) * fact(3) * fact(0))
        + fact(4) // (fact(2) * fact(1) * fact(1))
        + fact(2) // (fact(0) * fact(0) * fact(2))
    )


def TESTFUNC():
    a = 7
    for i in range(10):
        print(i + a)

    return 0


def NFact(x):
    def fact(x):
        _fact = 1
        for i in range(1, x + 1):
            _fact = _fact * i
        return _fact

    def r_NFact(num):
        twos = x - num
        ones = x - (2 * twos)
        if ones < 0:
            return 0
        return r_NFact(num - 1) + (fact(num) // (fact(ones) * fact(twos)))

    return r_NFact(x)


def N(x):
    if x < 0:
        return 0
    if x == 0 or x == 1:
        return 1
    return N(x - 1) + N(x - 2)


def N135(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    return N135(x - 1) + N135(x - 3) + N135(x - 5)


def NArr(x, arr):
    if x < 0:
        return 0
    if x == 0:
        return 1
    return sum([NArr(x - i, arr) for i in arr])


def main():
    #NFactArr(10, [1,3,5])
    #return
    print(NFact135())

    for n in range(10 + 1):
        print(n, NFact(n))

    for n in range(10 + 1):
        print(n, N(n))

    for n in range(10 + 1):
        print(n, N135(n))

    for n in range(10 + 1):
        print(n, NArr(n, [1, 3, 5]))


if __name__ == "__main__":
    main()
