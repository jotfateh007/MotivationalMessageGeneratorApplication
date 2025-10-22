import json
import getpass
import accountCreation as ac
import main
def login_screen():
    print('=' * 50)
    print("Log In to Hype-It-Up")
    print('=' * 50)

    username = input("\nPlease enter your username: \n>")
    with open('users.json', 'r') as f:
        data = json.load(f)

    userFound = False

    for i in data['user_details']:
        if i.get('user_name') == username:
            print("User found")
            userFound=True
            attempts = 3
            while attempts > 0:
                password = getpass.getpass("\nEnter your password:\n>")
                if i.get('pass_word') == password:
                    print("\nLogin successful! Redirecting to the homepage")
                    return username
                else:
                    attempts -= 1
                    print(f"Password incorrect! {attempts} attempts left.")
                
                if attempts == 0:
                    print("Too many failed attempts. Try again later.")

    
    if not userFound:
        createAccount = input("User not Found! Would you like to create an account?(y/n)")
        match createAccount:
            case 'y':
                ac.createAccount(username)
                return username
            case 'n':
                response = input("Would you like to try entering a different username?(y/n)")
                while (response != 'y' or response != 'n'):
                    if response == 'y':
                        username = login_screen()
                        return username
                    elif response == 'n':
                        print("\nExiting... Goodbye!\n")
                        return
                    else:
                        response = input("Invalid option. Please enter 'y' or 'n'")
            case _:
              return   


    