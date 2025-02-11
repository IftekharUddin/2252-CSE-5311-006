def fib(n):
    input(f"Entering fib({n})... Press Enter to continue.")

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

fib(5)
