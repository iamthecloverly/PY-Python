class kek:
    def __init__(self, data):
        self.data = data


# Add elements to the list
a = kek(1)
b = kek(2)
c = kek(3)
d = kek(4)
e = kek(5)

# Add the address on next element for each node
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

s = a

x = 0

while s!= None:
    if s.data % 2 == 0:
        print(s.data)
    s = s.next