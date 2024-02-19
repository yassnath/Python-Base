todos = ["wake up", "coding", "the rest"]
print(todos.index("coding")) # 1
print(todos.pop()) # code
print(todos) # ['wake up', 'the rest']
todos.append("music")
print(todos) # ['wake up', 'the rest', 'music']
todos.reverse()
print(todos) # ['music', 'the rest', 'wake up']
todos.remove("music")
print(todos) # ['the rest', 'wake up']
todos.extend(["analyse", "think"])
print(todos) # ['the rest', 'wake up', 'analyse', 'think']
todos.sort()
print(todos) # ['analyse', 'the rest', 'think', 'wake up']