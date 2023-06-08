a = {1,2,3,4,5,6,7,8,9,10}
b = {2,4,6,8,10,12,14,16,18,20}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

print(a | b)
print(a & b)
print(a - b)