def sum_of_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)

env = input("Please enter your environment (dev/staging/prod): ")
print("Environment entered:", env)

if env == "prod":
    sum_of_num()