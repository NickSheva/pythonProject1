import timeit
def test():
    """Stupid test function"""
    x = [i for i in range(100)]
    return x
print(test())
if __name__ == '__main__':

    print(timeit.timeit("test()", setup="from __main__ import test"))



def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

print(f(2), g(2), h(2))

if __name__ == '__main__':
    print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))