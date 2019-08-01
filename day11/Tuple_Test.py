t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])
print(t1 == t2) #True
print(id(t1[-1])) #2336758784648
t1[-1].append(5)
print(t1) #(1, 2, [3, 4, 5])
print(id(t1[-1])) #2336758784648
print(t1 == t2) #False

tuple