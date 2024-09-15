try:
    #answer = 10/0
    number = int(input("Enter a number: "))
    print(answer)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")