
a = int(input("Number A: "))
b = int(input("Number B: "))
c = str(input("Operation: "))

if c == "/" and a == 0:
    print("Division by zero is forbidden")
elif c == "+":
    print(f'Result: {a + b}')
elif c == "-":
    print(f'Result: {a - b}')
elif c == "*":
    print(f'Result: {a * b}')
elif c == "/":
    print(f'Result: {a / b}')
else:
    print("Forbidden operation")
