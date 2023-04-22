import re
if re.match("[6-9][0-9]{9}$",input()):
    print("Valid phone number")
else:
    print("Invalid phone number")