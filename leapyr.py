def leap(n):
    if (n % 4 == 0) and (n % 400 == 0):
        print('yes')
    elif n%4 == 0:
        print('yes')
    else:
        print('no')
n = int(input())
leap(n)