from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'You Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if(player_input == computer_input):
        winner_label.config(text = "Tie",font="arial 20 bold")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner_label.config(text="You Won!!!",font="arial 20 bold")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!",font="arial 20 bold")
        computer_score_label.config(text='Your Score : ' + str(computer_score))

def get_computer_choice():
    return random.choice(options)
game_window = Tk()
game_window.title("--Rock Paper Scissor Game--")
app_font = font.Font(size = 12)
game_title = Label(text = 'Rock Paper Scissor', font ="arial 20 bold underline", fg = 'black')
game_title.pack()
winner_label = Label(text = "Let's Start the Game...", fg = 'dark green', font ="arial 20 bold", pady = 8)
winner_label.pack()
input_frame = Frame(game_window)
input_frame.pack()

player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'grey')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 20, bd = 1, bg = '#29e345',font="arial 10 bold", pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 20, bd = 1, bg = '#f2ec3f',font="arial 10 bold", pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 20, bd = 1, bg = '#fa559a',font="arial 10 bold", pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

score_label = Label(input_frame, text = 'Score : ', font = app_font, fg = 'grey')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'You Selected : ---', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : -', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : -', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

game_window.geometry('700x400')
game_window.mainloop()