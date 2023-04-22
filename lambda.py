n = list(map(str, input().split()))
k = input()
x = list(filter(lambda x: k == x,n))
print(x)
