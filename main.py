import login as l
import accountCreation as ac
import messageGeneration as mg
import messageLogging as ml
import preferences
import sendEmail as se
import time
import atexit


def getContent(username):
    userPrefs = preferences.get_user_preferences(username)
    if userPrefs:
        name = userPrefs['name']
        age = userPrefs['age']
        answerChoice = input("Press 1 for a generic AI-generated message and press 2 for a custom-generated message\n> ")
        
        while answerChoice not in ('1', '2'):
            answerChoice = input("Invalid choice! Please enter a valid choice (1 or 2)\n> ")
        
        if answerChoice == '1':
            content = f"Generate a motivational message for the user. {name} is their name, and they are {age} years old."
        elif answerChoice == '2':
            toAdd = input("Enter a personalized story or other information for your personalized message:\n> ")
            content = f"Generate a motivational message for the user. {name} is their name, they are {age} years old, and the following prompt is provided in parentheses ({toAdd})."
        
        return content
    else:
        content = None
        return content
    


def AIMicroService(username):
    message = getContent(username)
    prefs = preferences.get_user_preferences(username)
    narrate = prefs['narration']
    if message:
        with open ('AI.txt', 'r+') as file:
            file.seek(0)
            file.truncate()
            file.write(f'generate\n{message}')
            file.seek(0)
            done = file.readline()
            while done != 'done':
                print("Generating...")
                time.sleep(3)
                file.seek(0)
                done = file.readline().strip()
            message = file.read().strip()    
            print(message)
            ml.log_user_history(username, message)
        if narrate == 'yes':
            with open ('narrate.txt', 'r+')as nar:
                nar.seek(0)
                nar.truncate()
                nar.write(f'translate\n{username}\n{message}')
                isDone = nar.readline().strip()
                while isDone != 'done':
                    time.sleep(3)
                    print("Narrating message...")
                    nar.seek(0)
                    isDone = nar.readline().strip()
        print("\nReturning to home page...")
        time.sleep(2)
        home_page(username)
        return
    else:
        print ("Please enter valid preferences first!")
        print ("Returning to homepage...")
        time.sleep(1.5)
        home_page(username)
        return







def music_menu(username):
    
    print(f"\nThis is the music menu,  {username}!")
    print("Select one of the following options:\n")
    print("[1] Play Track")
    print("[2] Pause Track")
    print("[3] Resume Track")
    print("[4] Restart Track")
    print("[5] Stop Track")
    print("[6] Skip Track")
    print("[7] Go back to main menu")

    chosenChoice =input('\nEnter an option> ')
    match chosenChoice:
        case '1':
            toWrite ="Play"
        case '2':
            toWrite = "Pause"
        case '3': 
            toWrite ="Resume"
        case '4':
            toWrite = "Restart"
        case '5':
            toWrite = 'Stop'
        case '6':
            toWrite ="Skip"
        case '7':
            home_page(username)
            return
        case _:
            print("\nInvalid choice. Try again.\n")
            music_menu(username)

    with open("music.txt", 'r+') as file:
        file.seek(0)
        file.truncate()
        file.write(toWrite)
    print("Command recieved")
    print("Returning to music music menu...")
    time.sleep(1)
    music_menu(username)
    



    




def home_page(username):
    print(f"\nWelcome back, {username}!")
    print("Here you can access motivational messages and more!\n")
    print("[1] Set Preferences")
    print("[2] Download User History")
    print("[3] Send Motivational Email")
    print("[4] Generate a Motivational Message")
    print("[5] Have AI Generate A Message")
    print("[6] Open Music Menu")
    print("[7] Logout")

    choice = input("\nChoose an option: ")

    if choice == "1":
        preferences.display_preferences(username)
    elif choice == "2":
        ml.download_user_history(username)
    elif choice == "3":
        se.sendEmail(username)
    elif choice == "4":
        mg.generateMessage(username)
    elif choice =='5':
        AIMicroService(username)

    elif choice == '6':
        music_menu(username)
    elif choice == "7":
        print("\nLogging out... Returning to the main menu.\n")
        main()
    else:
        print("\nInvalid choice. Try again.\n")
        home_page(username)





def display_menu():
    print("=" * 50)
    print("Welcome to Hype-It-Up!")
    print("=" * 50)
    print("\nThis is a motivational message generation program to make you feel better.\n")
    print("\n Please choose one of the following options:\n")
    print("[1] Login")
    print("[2] Register")
    print("[3] Exit\n")
    choice = input("Type the number corresponding to your choice:\n> ")
    return choice


def send_command_to_microservice():
    with open ('music.txt', 'r+') as file:
        file.seek(0)
        file.truncate()
        file.write('stop')



atexit.register(send_command_to_microservice)


def main():
    choice = display_menu()
    if choice == "1":
        print("\nYou selected Login.\n")
        username = l.login_screen()
        if username:
            home_page(username)
    elif choice == "2":
        print("\nYou selected Register.\n")
        username = ac.createAccount('')
        if username:
            home_page(username)
    elif choice == "3":
        print("\nExiting... Goodbye!\n")
    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.\n")
        choice = display_menu()

if __name__ == "__main__":
    main()
