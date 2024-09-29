print("The Age Calculator")
print()
first_name = (input("Enter First Name: "))
last_name = (input("Enter Last Name: "))
current_year = int(input("Enter the Current Year: "))
birth_year = int(input("Enter Your Birth Year: "))
print()
age = current_year-birth_year
print("Hello " + first_name + " " + last_name + "!\nYou are " + str(age) + " years old this year.")
age += 1
print()
print(f"You will be {age} years old next year!")
print()
print(" by, Cody Hobbs")