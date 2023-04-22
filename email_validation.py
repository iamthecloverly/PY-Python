import re
n = input()
if re.match('[a-z0-9]+'+'@'+'[a-z]+'+'\.'+'[a-z]+', n):
    print("Yes")
else:
    print("no")

