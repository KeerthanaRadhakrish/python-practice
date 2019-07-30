#program to find if a person is a teenager

name = str(input("enter your name: "))
print(name)

age = int(input("enter your age: "))
print(age)

if age > 12 and age < 20:
    print("you are a teenager", name)
elif age < 12:
    print("you are a kid", name)
else: 
    print("you are old", name)


