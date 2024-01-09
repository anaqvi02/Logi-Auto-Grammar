import tkinter as tk
from dotenv import load_dotenv
import os
import subprocess
import pystray
from PIL import Image
import threading


class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Settings')
        self.root.geometry('300x200')

        load_dotenv()
        self.api_endpoint = os.getenv('API_END_POINT')
        self.api_key = os.getenv('API_KEY')
        self.model_id = os.getenv('MODEL_ID')

        self.api_endpoint_label = tk.Label(root, text='API Endpoint')
        self.api_endpoint_label.pack()
        self.api_endpoint_entry = tk.Entry(root)
        self.api_endpoint_entry.insert(0, self.api_endpoint)
        self.api_endpoint_entry.pack()

        self.api_key_label = tk.Label(root, text='API Key')
        self.api_key_label.pack()
        self.api_key_entry = tk.Entry(root)
        self.api_key_entry.insert(0, self.api_key)
        self.api_key_entry.pack()

        self.model_id_label = tk.Label(root, text='Model ID')
        self.model_id_label.pack()
        self.model_id_entry = tk.Entry(root)
        self.model_id_entry.insert(0, self.model_id)
        self.model_id_entry.pack()

        self.save_button = tk.Button(root, text='Save', command=self.save)
        self.save_button.pack()
        self.start_button = tk.Button(root, text='Start APP', command=self.start_hotkey)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text='Stop APP', command=self.stop_hotkey)
        self.stop_button.pack()

        self.hotkey_process = None

        self.icon = pystray.Icon("name", Image.open("icon.jpg"), "Icon", self.create_menu())
        threading.Thread(target=self.icon.run).start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_menu(self):
        return (pystray.MenuItem('Open', self.open_settings), pystray.MenuItem('Exit', self.exit))

    def open_settings(self):
        self.root.deiconify()

    def on_close(self):
        self.root.withdraw()

    def exit(self):
        self.icon.stop()
        self.root.after(500, self.root.quit)

    def start_hotkey(self):
        self.hotkey_process = subprocess.Popen(['python', 'hotkey.py'])

    def stop_hotkey(self):
        if self.hotkey_process:
            self.hotkey_process.terminate()
            self.hotkey_process = None

    def open_settings(self):
        self.root.deiconify()

    def save(self):
        self.api_endpoint = self.api_endpoint_entry.get()
        self.api_key = self.api_key_entry.get()
        self.model_id = self.model_id_entry.get()

        with open('.env', 'w') as f:
            f.write(f'API_END_POINT={self.api_endpoint}\n')
            f.write(f'API_KEY={self.api_key}\n')
            f.write(f'MODEL_ID={self.model_id}\n')

        self.root.iconify()


root = tk.Tk()
app = SettingsWindow(root)
root.withdraw()
root.mainloop()