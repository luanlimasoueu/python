from flask import Flask

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login_form():
    return "This is the login form"

@app.route("/login", methods=["POST"])
def login_auth():
    return "Processing your data"

@app.route("/login", methods=["DELETE", "PUT"])
def deny():
    return "This method is not allowed"

if __name__ == "__main__":
    app.run()