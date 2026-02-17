def add(a ,b):
    return a + b
def sub(a ,b):
    return a - b
def mul(a, b):
    return a * b
def div(a ,b):
    return a / b
print("simple calculator")
print("1; addition")
print("2: substraction")
print("3: multiplication")
print("4: division")
choice = int(input("Enter your choice(1-4) : "))

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))
if choice == 1:
    print("result", add(num1, num2))
elif choice == 2:
    print("result", sub(num1, num2))
elif choice == 3:
    print("result", mul(num1, num2))        
elif choice == 4:
    if num2 > 0:
        print("result", div(num1, num2))
    else:
        print("error: division by zero")    
else:
    print("invalid choice")

c