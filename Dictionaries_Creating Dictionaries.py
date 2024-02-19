capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
squares = {1:1, 2:4, 3:9}
print(squares) # {1: 1, 2: 4, 3: 9}
print(type(squares)) # <class 'dict'>
randoms = {1:"Bob", "17":False, "Blue":"Red"}
empty_dictionary = {}
print(type(empty_dictionary)) # <class 'dict'>
print("=======================")
tuple_of_tuples = (
 ("Indonesia", "Jakarta"),
 ("Italy", "Rome"),
 ("Germany", "Berlin")
)
capitals = dict(tuple_of_tuples)
print(capitals) # {'Indonesia': 'Jakarta', 'Italy': 'Rome', 'Germany': 'Berlin'}
list_of_tuples = [
 ("Indonesia", "Jakarta"),
 ("Italy", "Rome"),
 ("Germany", "Berlin")
]
capitals = dict(list_of_tuples)
print(capitals) # {'Indonesia': 'Jakarta', 'Italy': 'Rome', 'Germany': 'Berlin'}