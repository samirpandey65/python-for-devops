for i in range(5):
    env = input("Please enter your environment (dev/staging/prod): ")

    # Conditional statements
    if env == "PROD":
        print("Dont deploy on friday")
    elif env == "UAT":
        print("Deploy after testing")
    else:
        print("You can deploy")