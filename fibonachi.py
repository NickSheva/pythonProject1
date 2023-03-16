s = 10
x = [0, 1]
fib = x[0:2] + [x.append(x[-1] + x[-2]) or x[-1] for i in range(s-2)]
import timeit
print(timeit.timeit('fib', globals=globals()))
print()
print()
def fibo(n):
    if n < 0:
        return 'Enter number more zero'
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
import timeit
print(timeit.timeit('fibo', globals=globals()))
print()

def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]


import timeit
print(timeit.timeit('fibonacci', globals=globals()))
print()
def Fib_memoisation(n, memo={}):
    if n <= 0:
        return 'Введите число больше 0'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n not in memo:
            memo[n] = Fib_memoisation(n - 1, memo) + Fib_memoisation(n - 2, memo)
        return memo[n]
import timeit
print(timeit.timeit('Fib_memoisation', globals=globals()))

