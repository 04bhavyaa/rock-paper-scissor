from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Choices for the game
CHOICES = ["Rock", "Paper", "Scissors"]

# Helper function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "user"
    else:
        return "computer"

# Route to render the HTML page
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint to handle the game logic
@app.route("/play", methods=["POST"])
def play():
    user_choice = request.json.get("choice")
    computer_choice = random.choice(CHOICES)
    winner = determine_winner(user_choice, computer_choice)

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "winner": winner
    })

if __name__ == "__main__":
    app.run(debug=True)
