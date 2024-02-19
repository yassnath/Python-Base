todo_list = ["wake up", "coding", "the rest"]
print(todo_list[1]) # coffee
print(todo_list[-1]) # the rest
print(todo_list[:2]) # ['wake up', 'coffee']
print("play" in todo_list) # False
print("coding" in todo_list) # True
print(len(todo_list)) # 3

print("========================")

programmer_todo_list = ["set up", "coding", "sleep"]
programmer_todo_list = programmer_todo_list + ["love"]
print(programmer_todo_list)
programmer_todo_list[2] = "programming"
print(programmer_todo_list)
del programmer_todo_list[0] # in reality, we should set up first!
print(programmer_todo_list)