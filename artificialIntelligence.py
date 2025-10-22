import openai
from openai import OpenAIError
import preferences as p
import time
import main as home
import messageLogging as ml

def getAPIKey():
    with open ('api.txt', 'r') as file:
        key = file.read().strip()
        return key

def AIGenMessage (content):
    if content:
    
        client = openai.Client(
            base_url="https://openrouter.ai/api/v1",
            api_key=getAPIKey() )

        # Prepare messages
        messages1 = [{"role": "user", "content": content }]

        try:
            # Create chat completion
            completion = client.chat.completions.create(
                model="google/gemini-2.0-flash-lite-preview-02-05:free",
                messages=messages1
            )

            # Print the message content
            messageToPrint = completion.choices[0].message.content.split('\n', 1)[0]
            return (f'done\n{messageToPrint}')
        
        except openai.APIError as e:
            # Handle quota error
            if e.code == "insufficient_quota":
                print("Error: You have exceeded your quota. Please check your OpenAI account and purchase more credits.")
            else:
                print(f"OpenAI API Error: {e}")

        except OpenAIError as e:
            # Handle other OpenAI-related errors
            print(f"OpenAI Error: {e}")

        except Exception as e:
            # Handle any other unexpected errors
            print(f"Unexpected error: {e}")

    
while True:
    
    with open('AI.txt', 'r+', encoding='utf-8') as file:
        generate = file.readline().strip()
        if generate == "generate":
            content = file.read().strip()
            if content:
                file.seek(0)
                file.truncate()
                file.write(AIGenMessage(content))