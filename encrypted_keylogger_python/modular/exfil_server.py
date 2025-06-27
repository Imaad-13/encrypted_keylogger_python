from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    file.save("received_logs.txt")
    return "File received", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
