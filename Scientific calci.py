# Scientific Calculator in Python

import math

print("Scientific Calculator")

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 7:
        break

    if choice < 1 or choice > 7:
        print("Invalid choice")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
        print("Result: ", result)

    elif choice == 2:
        result = num1 - num2
        print("Result: ", result)

    elif choice == 3:
        result = num1 * num2
        print("Result: ", result)

    elif choice == 4:
        if num2 == 0:
            print("Error: Division by zero")
            continue
        result = num1 / num2
        print("Result: ", result)

    elif choice == 5:
        result = math.sqrt(num1)
        print("Result: ", result)

    elif choice == 6:
        result = num1 ** num2
        print("Result: ", result)