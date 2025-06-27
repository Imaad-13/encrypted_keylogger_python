# Encrypted Keylogger (Educational Project)

This project demonstrates the design and functionality of a simple keylogger with end-to-end encryption and simulated data exfiltration. The project is structured in two parts:

1. **Modular Approach** – Step-by-step implementation of each component involved in a secure keylogging system.
2. **Automated Version** – A fully functional one-click script that automates logging, encryption, server startup, and log exfiltration.

> Note: This project is intended for ethical, educational, and training purposes only. Do not use without the consent of the system owner.

---

## Project Structure

```
ENCRYPTED_KEYLOGGER_PYTHON/
│
├── keyloggerauto.py                # One-click full implementation
│
├── modular/
│   ├── encryptor.py                # Encrypts keystroke log with Fernet (AES)
│   ├── exfil_server.py             # Flask server to receive encrypted logs
│   ├── exfiltrate.py               # Sends encrypted logs to the server
│   ├── keylogger.py                # Basic keylogger that logs to log.txt
│   └── experimental_persist/
│       └── persistence.py          # Optional Windows Startup persistence
│
├── key.key                         # Symmetric encryption key (used in both flows)
├── log.txt                         # Raw keystroke log file
├── log_encrypted.txt              # AES-encrypted version of the log
├── received_logs.txt              # File received on server side
└── README.md                       # Project documentation
```

---

## 1. Modular Approach (`/modular/`)

The modular folder contains standalone scripts, each of which performs a specific task. This approach helps understand and test each stage of the system independently.

- `keylogger.py`  
  Captures keystrokes and logs them into `log.txt`.

- `encryptor.py`  
  Encrypts the captured log using AES (via Fernet from the `cryptography` library). Outputs to `log_encrypted.txt`.

- `exfil_server.py`  
  A simple Flask server that accepts `POST` requests and stores the uploaded file as `received_logs.txt`.

- `exfiltrate.py`  
  Client script that sends `log_encrypted.txt` to the running Flask server.

- `experimental_persist/persistence.py`  
  Optional script that copies the keylogger to the Windows startup directory for persistence (only for testing on Windows).

---

## 2. Automated Script (`keyloggerauto.py`)

This is a one-click script that:
1. Starts keylogging
2. On pressing `ESC`, stops the logger
3. Automatically encrypts the log
4. Launches the Flask server in a background thread
5. Sends the encrypted log to the server

Ideal for demonstrating the entire workflow in one run.

---

## How to Run

### Prerequisites:
Install required packages:
```bash
pip install pynput cryptography flask requests
```

### Recommended Run Order for Modular Approach:
```bash
# Step 1: Run the keylogger
python modular/keylogger.py

# Step 2: Encrypt the log
python modular/encryptor.py

# Step 3: Start the server
python modular/exfil_server.py

# Step 4: In a separate terminal, exfiltrate the file
python modular/exfiltrate.py
```

### Run One-Click Automated Version:
```bash
python keyloggerauto.py
```

---

## Disclaimer
This project is created for ethical learning, cybersecurity training, and demonstration purposes **only**. Deploying or distributing this software without permission is prohibited and may violate computer misuse laws.
