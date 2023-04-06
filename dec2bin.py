n = int(input())
sum,i = 0,1
while(n != 0):
    d = n%2
    n = n//2
    sum += d*i
    i = i*10
print(sum)