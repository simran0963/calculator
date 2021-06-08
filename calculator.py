x = input("enter first number ")
y = input("enter second number ")

x = int(x)
y = int(y)

choice = print("choose any one operation")
print("1. addition ")
print("2. subtraction ")
print("3. multiplication")
print("4. division")

choice = input("enter your operation ")
choice = int(choice)

if choice == 1 :
    print(x, "+", y)
    print(x+y)

elif choice == 2 :
    print(x, "-", y)
    print(x-y)

elif choice == 3 :
    print(x,"*", y)
    print(x*y)

elif choice == 4 :
    print(x, "/", y)
    print(x/y)

else :
    print("invalid input")