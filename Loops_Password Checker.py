password = input("Masukkan password: ")
real_password = "python123"

while password != real_password:
    print("That's not the right password!")
    password = input("Masukkan password: ")

print("Welcome!")
