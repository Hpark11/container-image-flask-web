import os
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

@app.route("/")
def main():
    return "Hello, World!\n"

@app.route('/respond')
def niceToMeetYou():
    return 'Nice to meet you\n'
