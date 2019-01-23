n = int(input(("Enter number of elements to be inserted to list")))
a = []
for i in range(0,n):
    elem = int(input("Enter number"))
    a.append(elem)

avg = sum(a)/n
print(avg)