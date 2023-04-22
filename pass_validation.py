import re
n = input()
if re.match('[a-zA-Z0-9_@]{8}$',n):
    print('valid pass')
else:
    print('invalid pass')