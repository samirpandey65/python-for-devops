#num = int(input("Enter the number: "))

#for i in range(1, 11):
#    print(f"{num} x {i} = {num*i}")


#string formatting
#name = input("Enter your name: ")

#print(f"Hello, {name}! Welcome to Python programming.")

#while loop
#samir = "shikha"

#while samir == "shikha":
#    print("samir is love to shikha")


#real world example for while loop
choice = input("Enter the q for quit: ")

while choice != "q":
    num = int(input("Enter the number: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    choice = input("Enter the q for quit: ")