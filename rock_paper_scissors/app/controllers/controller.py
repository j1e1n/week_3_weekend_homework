from app import app
from flask import render_template, request, redirect
from app.models.game import *
from app.models.player import Player


@app.route('/')
def index():
    return render_template("index.html", title="Home")

@app.route('/play')
def play_page():
    return render_template("play.html", title="Play")

@app.route('/winner', methods=['POST'])
def submit_choices():
    p1_name = request.form['player_1']
    p1_choice = request.form['choice_1']
    p2_name = request.form['player_2']
    p2_choice = request.form['choice_2']
    p1 = Player(p1_name, p1_choice)
    p2 = Player(p2_name, p2_choice)
    winner = Game.get_winner(p1, p2)
    return render_template("winner.html", title="Winner", winner=winner)




    # choice_1 = request.form['choice_1']
    # choice_2 = request.form['choice_2']
    # if choice_1 == "rock":
    #     if choice_2 == "scissors":
    #         return redirect('/rock/scissors')
    #     return redirect('/rock/paper')



    
        


    


