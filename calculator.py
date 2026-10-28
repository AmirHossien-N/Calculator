history = []
memory = 0
last_result = None

print("Calculator")
print("Operators: +  -  *  /  **")
print("h: History")
print("b: Convert last result to binary")
print("o: Convert last result to base 8")
print("x: Convert last result to base 16")
print("m+: Add last result to memory")
print("m: Show memory")
print("m-: Subtract last result from memory")
print("q: Quit")

while True:
    command = input("\n number/command >>: ").strip().lower()

    if command == "q":
        print("Good bye")
        break

    elif command == "h":
        if len(history) == 0:
            print("History is empty")
        else:
            for item in history:
                print(item)

    elif command == "m":
        print(":>", memory)

    elif command == "m+":
        if last_result is None:
            print("Error: None Calculating")
        else:
            memory = memory + last_result
            print(":>", memory)

    elif command == "m-":
        if last_result is None:
            print("Error: None Calculating")
        else:
            memory = memory - last_result
            print(":>", memory)

    elif command == "b" or command == "o" or command == "x":
        if last_result is None:
            print("Error: None Calculating")
        elif last_result != int(last_result):
            print("Just decimaly Numbers!")
        else:
            number = int(last_result)
            if command == "b":
                print(":> ", bin(number))
            elif command == "o":
                print(":> ", oct(number))
            else:
                print(":> ", hex(number))

    else:
        try:
            a = float(command)
            operator = input("(+ - * / **):> ").strip()
            b = float(input("number/command >>: "))

            if a == int(a):
                a = int(a)
            if b == int(b):
                b = int(b)

            if operator == "+":
                result = a + b
            elif operator == "-":
                result = a - b
            elif operator == "*":
                result = a * b
            elif operator == "/":
                if b == 0:
                    print("Zero is not allowed")
                    continue
                result = a / b
            elif operator == "**":
                result = a ** b
            else:
                print("The operator is invalid")
                continue

            if result == int(result):
                result = int(result)

            last_result = result
            history.append(str(a) + " " + operator + " " + str(b) + " = " + str(result))
            print(">> ", result)

        except ValueError:
            print("Input is invalid")
