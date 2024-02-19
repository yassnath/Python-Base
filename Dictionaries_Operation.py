# Retrieve the value of a key
capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
print(capitals["Italy"]) # Rome
print(capitals["Indonesia"]) # Jakarta
squares = {1:1, 2:4, 3:9}
print(squares[1]) # 1
print(squares[3]) # 9
print("==========================================================================")
# Get the value of a key
capitals = {"Indonesia":"Jakarta", "Italy":"Rome", "Germany":"Berlin"}
print(capitals.get("Italy")) # Rome
print(capitals.get("Indonesia")) # Jakarta
squares = {1:1, 2:4, 3:9}
print(squares.get(1)) # 1
print(squares.get(3)) # 9
print(squares.get(4)) # None
print(squares.get(4, "Not available!")) # Not available!
print("==========================================================================")
# Add & delete key-value pair, and check existence of key
capitals = {"Indonesia":"Jakarta", "Italy":"Rome"}
capitals["Japan"] = "Tokyo"
print(capitals) # {'Indonesia': 'Jakarta', 'Italy': 'Rome', 'Japan': 'Tokyo'}
capitals["Indonesia"] = "Penajam Paser Utara"
print(capitals) # {'Indonesia': 'Penajam Paser Utara', 'Italy': 'Rome', 'Japan': 'Tokyo'}
del capitals["Italy"]
print(capitals) # {'Indonesia': 'Penajam Paser Utara', 'Japan': 'Tokyo'}
print("Indonesia" in capitals) # True
print("France" in capitals) # False
print("==========================================================================")
# Length, update multiple key-value pairs, get all keys, and clear 
capitals = {"Indonesia":"Jakarta", "Italy":"Rome"}
print(len(capitals)) # 2
y = {"Germany":"Berlin", "France":"Paris"}
capitals.update(y)
print(capitals) # {'Indonesia': 'Jakarta', 'Italy': 'Rome', 'Germany': 'Berlin', 'France': 'Paris'}
capitals_keys = list(capitals.keys())
print(capitals_keys) # ['Indonesia', 'Italy', 'Germany', 'France']
capitals.clear()
print(capitals) # {}