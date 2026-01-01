# Get the Environment from user and print it
#env = input( "Please enter your environment (dev/staging/prod): " )

#print(env)

#typ casting - converting string to int ( 1 data type to another data type)
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#print("The addition of a and b is", a+b)
#print("The multiplication of a and b is", a*b)
#print("The subtraction of a and b is", a-b)
#print("The division of a and b is", a/b)

env = input("Please enter your environment (dev/staging/prod): ")

# Conditional statements
if env == "PROD":
    print("Dont deploy on friday")
elif env == "UAT":
    print("Deploy after testing")
else:
    print("You can deploy")
