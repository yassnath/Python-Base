n1 = int(input("Type first number: "))
n2 = int(input("Type second number: "))
try:
 print(n1/n2)
except ZeroDivisionError:
 print("Cannot divide by 0")