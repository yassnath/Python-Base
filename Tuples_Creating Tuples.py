nums = (3, 2, 1, 2)
nums_2 = 1, 2, 3
empty_tuple = ()
tuple_size_one = ("Borobudur",)
print(type(tuple_size_one)) # <class 'tuple'>
# compare that with the example below
this_is_not_tuple_1 = ("Borobudur")
print(type(this_is_not_tuple_1)) # <class 'str'>
this_is_not_tuple_2 = (4)
print(type(this_is_not_tuple_2)) # <class 'int'>
print("========================")
x = tuple("abc")
print(x) # ('a', 'b', 'c')
y = tuple([2, 1, 2, 1])
print(y) # (2, 1, 2, 1)
z = tuple(range(3))
print(z) # (0, 1, 2)
w = tuple()
print(w) # ()
