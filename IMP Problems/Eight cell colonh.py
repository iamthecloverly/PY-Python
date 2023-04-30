l = list(map(int, input().split()))
days = int(input())
l = [0] + l + [0]
while days != 0:
    ls = []
    for i in range(1, len(l) - 1):
        ls.append(l[i - 1] ^ l[i + 1])
    l = [0] + ls + [0]
    days -= 1
print(*l[1:len(l) - 1])
