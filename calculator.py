def calculator():
    print("=== Python Calculator ===")
    
    while True:
        try:
            num1 = float(input("nEnter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose operation +, -, *, / or 'q' to quit: ")
            
            if operation == 'q':
                print("Calculator closed. Bye! 👋")
                break
                
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation! Use +, -, *, / only")
                continue
                
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError:
            print("Error: Please enter valid numbers only!")

calculator()
