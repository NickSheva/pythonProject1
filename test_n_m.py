def plus(a, b):
    print(a+b)

def minus(a,b):
    print(a - b)

plus(4, 5)
minus(10, 3)

if __name__ == "__main__":
    print("This answer is from 'test_n_m.py'")

def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)
print(fac(4))

def fib(n):
    if n < 0:
        return 0
    elif n == 1 and n == 2:
        return 1
    else:
       return fib(n-1) + fib(n-2)

print(fib(6))
