print ("1 - ADD")
print ("2 - SUBTRACTION")
print ("3 - MULTIPLY")
print ("4 - DIVIDE")
option = int(input("CHOOSE AN OPERATION"))

if (option in [1, 2, 3, 4]):
    num1 = int(input("ENTER YOUR FIRST NUMBER"))
    num2 = int(input("ENTER YOUR SECOND NUMBER"))

    if (option == 1):
        result = num1 + num2

    elif (option == 2):
        result = num1 - num2

    elif (option == 3):
        result = num1 * num2

    elif (option == 4):
        result = num1 // num2

    print("THE RESULT OF THE OPERATION IS {}".format(result))

else:
    print("INVALID OPERATION ENTERED")
