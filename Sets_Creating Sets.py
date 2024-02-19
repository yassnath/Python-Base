s1 = set("text")
print(s1) # {'t', 'x', 'e'}
s2 = set([0,0,0,1])
print(s2) # {0, 1}
empty_set = set()
print(empty_set) # set()
print(type(empty_set)) # <class 'set'>
# the following is an empty dictionary, not an empty set
empty_dict = {}
print(type(empty_dict)) # <class 'dict'>
print("=====================")
nums = {5, 2, 3, 1}
letters = {'a', 'b', 'c'}
singleton = {0.5}
# duplicates are removed
s1 = {1, 1, 1, 1, 2}
print(s1) # {1, 2}
# unlike list, sets do not record element position
s2 = {3, 1, 2}
print(s2) # {1, 2, 3}