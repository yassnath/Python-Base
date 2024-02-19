s = {5, 1, 2, 7, 7}
print(s) # {1, 2, 5, 7}
print(len(s)) # 4
print(7 in s) # True
print(8 in s) # False
print(8 not in s) # True
s.add(3)
print(s) # {1, 2, 3, 5, 7}
s.remove(7)
print(s) # {1, 2, 3, 5}
s.update({5, 6})
print(s) # {1, 2, 3, 5, 6}
print("=====================")
# Intersection, union, difference, and symmetric difference
s1 = {1, 2, 5}
s2 = {2, 3}
print(s1 & s2) # {2}
print(s1 | s2) # {1, 2, 3, 5}
print(s1 - s2) # {1, 5}
print((s1 - s2) | (s2 - s1)) # {1, 3, 5}
print(s1 ^ s2) # {1, 3, 5}
print("=====================")
# Intersection, union, difference, and symmetric difference
s1 = {1, 2, 5}
s2 = {2, 3}
print(s1.intersection(s2)) # {2}
print(s1.union(s2)) # {1, 2, 3, 5}
print(s1.difference(s2)) # {1, 5}
print(s1.symmetric_difference(s2)) # {1, 3, 5}
print("=====================")
# Subset/Superset
s1 = {1, 2}
s2 = {1, 2, 3}
s3 = {3, 4}
print(s1 <= s2) # True
print(s2 >= s1) # True
print(s1 <= s3) # False
print(s1 <= s1) # True