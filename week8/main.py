# Memoize time
_Fib = {}

def fibonacci(n):
    if (n == 0) or (n == 1):
        return 1
    if n not in _Fib:
        _Fib[n] = fibonacci(n-1) + fibonacci(n-2)
    return _Fib[n]

for i in range(10000):
    print(i, fibonacci(i))