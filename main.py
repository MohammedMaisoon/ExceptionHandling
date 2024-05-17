num1 = int(input("Enter First Number to Divide:"))
num2 = int(input("Enter Second Number to Divide:"))
try:
    calc = num1/num2
    print(calc)
except ZeroDivisionError:
    print("The Number Cannot Be Divided By Zero")

