from flask import Flask, request, jsonify, send_from_directory
import re

app = Flask(__name__)

def check_password_strength(password):
    length_score = min(len(password) // 8, 3)
    diversity_score = len(set(password))
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    score = length_score + diversity_score + has_uppercase + has_lowercase + has_digit + has_special
    if score < 5:
        strength = "Weak"
    elif score < 8:
        strength = "Moderate"
    else:
        strength = "Strong"
    return strength, score

@app.route('/check_strength', methods=['POST'])
def check_strength():
    data = request.get_json()
    password = data['password']
    strength, score = check_password_strength(password)
    return jsonify({'strength': strength, 'score': score})

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
