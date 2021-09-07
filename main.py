# Request Pin from user
selectedPin = input("Enter PIN: ")

# Set Logged in value to 1 now user is logged in
loggedIn = 1

while loggedIn == 1:
    # Print menu options
    print("1 - Check Balance")
    print("2 - withdraw")
    print("3 - End Session")
    # Get selection Input
    selection = input("Enter Selection: ")

    # Selection 1
    if selection == 1:
        print("Balance")
    # Selection 2
    elif selection == 2:
        print("How much would you like to withdraw")
    # Selection 3
    elif selection == 3:
        print("logging out")
        # Log out user (exit loop)
        loggedIn = 0
    else:
        print("Invalid selection")