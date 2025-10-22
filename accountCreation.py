import json
import main
def createAccount(givenName):
    if not givenName:
        givenName = input("Please enter a unique username (or \'back\' to return to the main menu)\n>")
    if givenName.lower() == 'back':
        print("Returning to main menu")
        main.main()
        return

    with open('users.json', 'r+') as file:
        toRead = json.load(file)
    for user in toRead['user_details']:
        if user.get('user_name') == givenName:
            print('Username already taken!')
            miniResponse = input("Would you like to return to the main menu? (y/n)\n>")
            while (miniResponse != 'y' and miniResponse != 'n'):
                 miniResponse = input("Invalid choice. Please enter 'y' or 'n'!")
            if miniResponse == 'y':
                print("Returning to main menu")
                main.main()
                return
            elif miniResponse=='n':
                createAccount('')
                return
    password = input("Enter a password:\n>")
    toRead['user_details'].append({"user_name": givenName, "pass_word": password})
    with open('users.json', 'w') as file:
        json.dump(toRead, file, indent=4)
    print(f"Account created successfully for {givenName}. Redirecting to homepage...")
    main.home_page(givenName)

    