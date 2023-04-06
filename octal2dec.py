n = int(input())
sum , i = 0, 1
while n!=0:
    d = n%8
    n = n//8
    sum += d*i
    i = i*10
print(sum)  #oct 2 dec