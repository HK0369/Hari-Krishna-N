class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add" or self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtract" or self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiply" or self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "divide" or self.operation == "division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error! Division by zero."
        else:
            return "Invalid operation!"


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (addition(add), subtraction(subtract), multiplication(multiply), division(divide)): ")

calc = Calculator(a, b, operation)
result = calc.calculate()

print("Result:", result)
