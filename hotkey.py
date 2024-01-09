import os
from openai import OpenAI
from dotenv import load_dotenv
import pynput
from pynput.keyboard import Key, Controller
import pyperclip
import platform
import time

if platform.system() == 'Darwin': 
    key = Key.cmd
else:
    key = Key.ctrl

load_dotenv() 
client = OpenAI(base_url=os.getenv('API_END_POINT'), api_key=os.getenv('API_KEY')) 
keyboard = Controller()
x = ""
def on_activate():
    keyboard.press(key)
    keyboard.press('c')
    time.sleep(0.1)
    keyboard.release('c')
    keyboard.release(key)
    time.sleep(0.1)
    x = pyperclip.paste()
    print("\nlipboard:",x)
    print("Starting AI call...")
    if x != "None":
        completion = client.chat.completions.create(
            model=os.getenv('MODEL_ID'),
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