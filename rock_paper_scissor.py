import random
from tkinter import *
from PIL import ImageTk, Image

# Main Window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="#2C3E50")

# Pictures - Resize images to 200x200
rock_img = ImageTk.PhotoImage(Image.open("rock-paper-scissor/rock-user.png").resize((200, 200)))
paper_img = ImageTk.PhotoImage(Image.open("rock-paper-scissor/paper-user.png").resize((200, 200)))
scissor_img = ImageTk.PhotoImage(Image.open("rock-paper-scissor/scissor-user.png").resize((200, 200)))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock-paper-scissor/rock.png").resize((200, 200)))
paper_img_comp = ImageTk.PhotoImage(Image.open("rock-paper-scissor/paper.png").resize((200, 200)))
scissor_img_comp = ImageTk.PhotoImage(Image.open("rock-paper-scissor/scissor.png").resize((200, 200)))

# Insert Pictures
user_label = Label(root, image=rock_img, bg="#2C3E50")
comp_label = Label(root, image=rock_img_comp, bg="#2C3E50")

user_label.grid(row=1, column=0, padx=20)
comp_label.grid(row=1, column=3, padx=20)

# Score
player_score = Label(root, text=0, font=("Helvetica", 30), bg="#2C3E50", fg="white")
comp_score = Label(root, text=0, font=("Helvetica", 30), bg="#2C3E50", fg="white")

player_score.grid(row=1, column=1, padx=20)
comp_score.grid(row=1, column=2, padx=20)

# Indicator
user_indicator = Label(root, font=("Helvetica", 20), text="USER", bg="#2C3E50", fg="white")
comp_indicator = Label(root, font=("Helvetica", 20), text="COMPUTER", bg="#2C3E50", fg="white")

user_indicator.grid(row=0, column=1, padx=20)
comp_indicator.grid(row=0, column=2, padx=20)

# Message
msg = Label(root, font=("Helvetica", 25), bg="#2C3E50", fg="white")
msg.grid(row=3, column=1, columnspan=3)

# Game Rules Section
game_rules = Label(root, font=("Helvetica", 12), text="Rock beats Scissors | Scissors beats Paper | Paper beats Rock", bg="#2C3E50", fg="white")
game_rules.grid(row=4, column=0, columnspan=4, pady=10)

# Update Message
def update_message(x):
    msg['text'] = x

# Update User Score
def updateUserScore():
    score = int(player_score["text"])
    score += 1
    player_score["text"] = str(score)

# Update Computer Score
def updateCompScore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)

# Check Winner
def checkWinner(player, computer):
    if player == computer:
        update_message("Tie!")
    elif player == "rock":
        if computer == "paper":
            updateCompScore()
            update_message("Computer Won!")
        else:
            updateUserScore()
            update_message("You Won!")
    elif player == "paper":
        if computer == "scissor":
            updateCompScore()
            update_message("Computer Won!")
        else:
            updateUserScore()
            update_message("You Won!")
    elif player == "scissor":
        if computer == "rock":
            updateCompScore()
            update_message("Computer Won!")
        else:
            updateUserScore()
            update_message("You Won!")

    # Stop the game if anyone reaches score 10
    if int(player_score["text"]) >= 10:
        update_message("You reached 10! You Win!")
        disable_buttons()
    elif int(comp_score["text"]) >= 10:
        update_message("Computer reached 10! Computer Wins!")
        disable_buttons()

# Disable Buttons After Match Ends
def disable_buttons():
    rock_button.config(state=DISABLED)
    paper_button.config(state=DISABLED)
    scissor_button.config(state=DISABLED)

# Update Choices
choices = ["rock", "paper", "scissor"]
def update_choice(x):
    # for computer
    comp_choice = choices[random.randint(0, 2)]
    if comp_choice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif comp_choice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWinner(x, comp_choice)

# Buttons with improved layout
button_frame = Frame(root, bg="#2C3E50")
button_frame.grid(row=5, column=1, columnspan=3, pady=20)

rock_button = Button(button_frame, height=2, width=15, text="Rock", bg="#FF3E4D", fg="white", font=("Helvetica", 15), command=lambda: update_choice("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = Button(button_frame, height=2, width=15, text="Paper", bg="#FAD02E", fg="white", font=("Helvetica", 15), command=lambda: update_choice("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissor_button = Button(button_frame, height=2, width=15, text="Scissor", bg="#0ABDE3", fg="white", font=("Helvetica", 15), command=lambda: update_choice("scissor"))
scissor_button.grid(row=0, column=2, padx=10)

# Add a Reset Button
def reset_game():
    player_score["text"] = "0"
    comp_score["text"] = "0"
    update_message("Game Reset! Choose an option.")
    rock_button.config(state=NORMAL)
    paper_button.config(state=NORMAL)
    scissor_button.config(state=NORMAL)

reset_button = Button(root, text="Reset Game", bg="#7D3C98", fg="white", font=("Helvetica", 15), command=reset_game)
reset_button.grid(row=6, column=1, columnspan=3, pady=20)

# Main loop
root.mainloop()
