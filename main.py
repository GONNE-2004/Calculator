import art


def add(n1 : float, n2 : float): # i used float becuase when dividing it always returns it plus to avoid future typeError
    return n1 + n2              # i used something called mypy, installed via pip which shows data-types of functions or if a function is untyped


def subtract(n1 : float, n2 : float):
    return n1 - n2


def multiply(n1 : float, n2 : float):
    return n1 * n2


def divide(n1: float, n2: float):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return float ("non")

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))
def formate_number(num : float):
    """returns integer if number is whole else float"""
    return int(num) if num.is_integer() else num

def get_number(prompt : str):
    """Ensure the user enter the correct data type"""
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a valid numer!")

def get_operation():
    """prevents the  program from crashing incase the user entered an invalid operation"""
    while True:
        print("Available operation:")
        for op in operations:
            print(op)
            if op in operations:
                return op
            print(f"\n{op} not in the avaliable operations")



def calculator():
    """holds the main logic"""
    history = []
    while True: #main loop which keeps the program in repeat
        print(art.logo)
        should_accumulate = True
        num1 =get_number("What is the first number?: ") #asks the user for input but i used function with input to ask the user here, the logic is explained using doc str

        while should_accumulate:
            for symbol in operations:
                print(symbol)

            operation_symbol = get_operation("Pick an operation: ")
            num2 =get_number("What is the next number?: ") #asking for the 2nd input, used function with inputs instead of just input function
            answer = formate_number(operations[operation_symbol](num1, num2)) # initiated a new variable then assigned the dic name plus the key name in order to use the value which's an int
            cal_formate = f"{formate_number(num1)} {operation_symbol} {formate_number(num2)} = {formate_number(answer)} "
            #above i tried to check if the initial number were float or integer in order to return the final input as first entered
            print(cal_formate)

            history.append(cal_formate)#here i used append instead of (+=) because it'll the ans as singlw entity into the history list
            #whereas if i used (+=) it would have unpacked the ans as separate entity!!
            choice = input(f"\nType 'y' to continue with:{answer},type 'n' to start a new calculation,'Q' to exit program &'h' to review history. ").lower()

            if choice == "y":
                num1 = answer
            elif choice == "h":
                for item in history:
                    print(item)
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
