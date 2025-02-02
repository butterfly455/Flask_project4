from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.json['choice']
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a draw! 🤝"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win! 🎉"
    else:
        result = "You lose! 😢"

    return jsonify({
        "computer_choice": computer_choice,
        "result": result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)