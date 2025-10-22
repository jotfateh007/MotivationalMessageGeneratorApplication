import json
import time
import main

def load_user_history():
    with open('user_history.json', 'r') as file:
        data = file.read().strip()
        if not data: 
            return {}
        return json.loads(data)



def save_user_history(user_history_dict):
    with open('user_history.json', 'w') as file:
        json.dump(user_history_dict, file, indent=4)

def log_user_history(username, message, email_sent=False):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    status = "Emailed" if email_sent else "Generated"

    user_history_dict = load_user_history()

    history_entry = f"{current_time} - {status} - {message}"

    if username not in user_history_dict:
        user_history_dict[username] = []

    user_history_dict[username].append(history_entry)

    save_user_history(user_history_dict)

def get_user_history(username):
    user_history_dict = load_user_history()

    if username in user_history_dict:
        return user_history_dict[username]
    else:
        return None

def write_user_history_to_file(username):
    user_history = get_user_history(username)

    if user_history:
        with open(f"{username}_history.txt", 'w') as file:
            for entry in user_history:
                file.write(f"{entry}\n")
        print(f"History for {username} written to {username}_history.txt")
    else:
        print(f"No history found for {username}")


def print_user_history_to_terminal(username):
    user_history = get_user_history(username)

    if user_history:
        print(f"History for {username}:")
        for entry in user_history:
            print(entry)
    else:
        print(f"No history found for {username}")


def download_user_history(username):
    print("This is your user history, " + username + ": ")
    print_user_history_to_terminal(username)
    response = input("Would you like to download this user history?(y/n)\n>")
    while (response != 'y' and response != 'n'):
        response = input("Invalid response! Please enter 'y' or 'n'")
    if response == 'y':
        write_user_history_to_file(username)
        print("Returning to homepage")
        time.sleep(2)
        main.home_page(username)
        return

    elif response == 'n':
        print("History not downloaded! Returning to homepage!")
        time.sleep(2)
        main.home_page(username)
        return





