n = int(input())
sum , i = 0, 1
while n!=0:
    d = n%10
    n = n//10
    sum += d*i
    i = i*2
print(sum)  #bin 2 dec