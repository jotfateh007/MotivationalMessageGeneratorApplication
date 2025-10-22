import main
import time
import messageLogging
import preferences
import subprocess


def call_microservice():
    categories = ['general', 'exercise', 'study', 'work']
    category = input('Enter category (general, exercise, study, work): ') 
    while category not in categories:
        category = input('Invalid option. Enter a valid category (general, exercise, study, work): ') 
    
    with open('messageGen.txt', 'r+', encoding='utf-8') as file:
        file.seek(0)
        file.truncate()
        file.write(f'generate\n{category}')
        file.seek(0)
        done = file.readline().strip()
        while done != 'done':
            time.sleep(2)
            file.seek(0)
            done = file.readline().strip()
        result = file.read().strip()
    return result

def generateMessage(username):
    inMessage=call_microservice()
    personalizedData = preferences.get_user_preferences(username)
    if personalizedData:
        person_name = personalizedData['name']
        narrate = personalizedData['narration']
        personalizedMessage = inMessage.replace("{name}", person_name)
        print("Here is your personalized message:\n" + personalizedMessage)
        if narrate == 'yes':
            with open('narrate.txt', 'r+') as n:
                n.seek(0)
                n.truncate()
                n.write(f'translate\n{username}\n{personalizedMessage}')
                print("Narrating message...")
                n.seek(0)
                done = n.readline().strip()
                while done != 'done':
                    time.sleep(3)
                    print("Narrating message...")
                    n.seek(0)
                    done = n.readline().strip()
        messageLogging.log_user_history(username, personalizedMessage)
        print("Returning to home page...")
        time.sleep(1.5)
        main.home_page(username)
    else:
        print("Please go and enter preferences first!")
        print("Returning to homepage...")
        time.sleep(1)
        main.home_page(username)
        return

def generateEmailMessage(username):
    inMessage = call_microservice()
    personalizedData = preferences.get_user_preferences(username)
    person_name = personalizedData['name']
    personalizedMessage = inMessage.replace("{name}", person_name)
    return personalizedMessage
