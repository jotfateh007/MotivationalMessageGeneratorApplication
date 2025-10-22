import smtplib, ssl
import preferences as pref
import messageGeneration as mg
import messageLogging
import time
import main

def sendEmail(username):
    userPreferences = pref.get_user_preferences(username)
    if userPreferences:
        user_email = userPreferences['email']
        
        port = 465  
        smtp_server = "smtp.gmail.com"
        sender_email = "cs361demo@gmail.com"
        receiver_email = user_email
        password = 'qpch eooj gqfa kray'
        message = mg.generateEmailMessage(username)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email sent!")
        messageLogging.log_user_history(username, message, True)
        print("Returning to home page...")
        time.sleep(1.5)
        main.home_page(username)
    else: 
        print ("Please enter valid preferences first!")
        print ("Returning to homepage...")
        time.sleep(1.5)
        main.home_page(username)
        return
