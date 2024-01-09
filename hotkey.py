import pynput
from pynput.keyboard import Key, Controller
import pyperclip
from openai import OpenAI
client = OpenAI(base_url='https://api.naga.ac/v1', api_key='ng-BWRQIk7QUdfEP6ZJhJMSuad9Gt1sf') #NAGA KEY HERE
keyboard = Controller()
x = ""
def on_activate():
    keyboard.press(Key.cmd)
    keyboard.press('c')
    keyboard.release(Key.cmd)
    keyboard.release('c')

    x = pyperclip.paste()
    print("\nlipboard:",x)
    print("Starting AI call...")
    if x != "None":
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system",
                "content": "You are the grammar-bot. You take in a sentence, and return the sentence back with corrected grammar. You only return the sentence, nothing else. You only return the corrected sentence. Example: (user) 'Hello guyz' Mistral: 'Hello guys'"},
                {"role": "user", "content": x},
            ]
        )
    else:
        print("No text in clipboard")
    print(completion.choices[0].message.content)
    keyboard.tap(Key.delete)
    keyboard.type(completion.choices[0].message.content)
with pynput.keyboard.GlobalHotKeys({'<ctrl>+0': on_activate}) as h:
    h.join()