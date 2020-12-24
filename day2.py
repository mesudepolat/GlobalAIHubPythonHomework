list = []
name = input("Please enter a name: ")
lastname = input("Please enter a lastname: ")
age = int(input("Please enter an age: "))
dateofbirth = int(input("Please enter a date of birth (just year): "))
list.append([name,lastname,age,dateofbirth])

for i in list:
    print(i)

list = f"{name} {lastname} {age} {dateofbirth}"
print(list)

if age >= 18:
    print("You can go out to the street")

elif age > 0 and age <=18:
    print("You can't go out because it's too dangerous")

else:
    print("You entered your age wrong")