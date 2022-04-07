print("1.ADD \n2.SUB \n3.MUL\n4.DIV\n5.EXIT")
opt = int(input("Enter your option : "))
while opt < 5:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    if opt == 1:
        print(a+b)
    elif opt == 2:
        print(a-b)
    elif opt == 3:
        print(a*b)
    elif opt == 4:
        print(a/b)
    
    opt = int(input("Enter your next choice : "))
    
print("Successfully exit from the calculator.")
