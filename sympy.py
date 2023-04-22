import sympy

n = list(map(int, input().split()))
x = list(filter(lambda x: sympy.isprime(x) == 1, n))
print(x)
