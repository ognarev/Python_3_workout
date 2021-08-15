# Exceptions

def calculator(num1, num2, operator):
    """Simple number clculator. Can addition, subtruction, mulitplication, division."""
    if operator == '+':
        return f"{num1} {operator} {num2} = {num1 + num2}"
    elif operator == '-':
        return f"{num1} {operator} {num2} = {num1 - num2}"
    elif operator == '*':
        return f"{num1} {operator} {num2} = {num1 * num2}"
    elif operator == '/':
        try:
            return f"{num1} {operator} {num2} = {num1 / num2}"
        except ZeroDivisionError as ex:
            raise ArithmeticError() from None
    else:
        print("Operation can't be done with your operator. Use '+', '-', '*', '/'")

def main():
    num1 = input('Write first argument: ')
    try:
        num1 = int(num1)
        num2 = input('Write second argument: ')
        try:
            num2 = int(num2)
            operator = input('Write operator please: ')
            print(calculator(num1, num2, operator))
        except ValueError as ex:
            print("Second argument must be a number")
    except ValueError as ex:
        print("First argument must be a number")
    
if __name__ == '__main__':
    main()    