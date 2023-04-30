str1,str2 =  input().split()
l1 = len(str1)
l2 = len(str2)
l = [[0 for _ in range(l1+1)] for _ in range(l2+1)]
for i in range(1,l2+1):
    for j in range(1,l1+1):
        if str2[i-1] == str1[j-1]:
            l[i][j] = l[i-1][j-1]+1
        else:
            l[i][j] = max(l[i-1][j],l[i][j-1])
print(l[-1][-1])
