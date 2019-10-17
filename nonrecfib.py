#!/usr/bin/python3
"""Document Comment."""


def non_r_fib(num):
    """Non Recursive Nth Fibonacci sequence."""
    tot, x_2, x_1 = 1, 0, 1
    for _ in range(num):
        tot = x_1 + x_2
        x_2, x_1 = x_1, tot

    return tot


def main():
    """Test fib function."""
    print(non_r_fib(0))
    print(non_r_fib(44))
    print(non_r_fib(115))
    print(non_r_fib(1000))


if __name__ == "__main__":
    main()
