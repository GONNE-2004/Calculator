import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    while True: #main loop which keeps the program in repeat
        print(art.logo)
        should_accumulate = True
        num1 = float(input("What is the first number?: "))

        while should_accumulate:
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What is the next number?: "))
            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(f"\nType 'y' to continue calculating with:{answer} ,type 'n' to start a new calculation or 'Q' to exit program. ").lower()

            if choice == "y":
                num1 = answer
            elif choice == "q":
                print("GOODBYE!")
                return
            else:
                should_accumulate = False
                print("\n" * 20)
                break # this break takes the progeam back to the first while loop
                       #earlier i had called the function within the function but now i changed to using loops
                       # the problem with recursion it isn't memory efficient

calculator()
