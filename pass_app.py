from flask import Flask, render_template, request
import hashlib
import random
import string

app = Flask(__name__)

def generate_stronger_password():
    password_length = random.randint(20, 30)
    characters = string.ascii_letters + string.digits + string.punctuation
    stronger_password = ''.join(random.choice(characters) for i in range(password_length))
    return stronger_password

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if len(password) < 12:
        return "Moderate"
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
        return "Strong"
    return "Moderate"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        stronger_password = generate_stronger_password()
        return render_template("index.html", strength=strength, password=hashed_password, stronger_password=stronger_password)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, port=5001)
