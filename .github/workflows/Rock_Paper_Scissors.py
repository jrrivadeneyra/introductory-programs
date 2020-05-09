#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

#Valid input#
def valid_input(prompt, opt1, opt2, opt3):
    while True:
        response = input(prompt).lower()
        if opt1 == response:
            break
        elif opt2 == response:
            break
        elif opt3 == response:
            break
    return response

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
 
# Defines Random Player Subclass #
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# Defines Human Plaer Subclass #
class HumanPlayer(Player):
    def move(self):
        hp_move = valid_input("Rock, Paper, or Scissors?: ", 'rock', 'paper', 'scissors')
        return hp_move

# Defines Reflect Player Subclass #
class ReflectPlayer(Player):
    def learn(self, my_move, their_move):
        if my_move == 'rock':
            def move(self):
                return 'rock'
        elif my_move == 'paper':
            def move(self):
                return 'paper'
        elif my_move == 'scissors':
            def move(self):
                return 'scissors'
        
# Defines Cycle Player Subclass #
class CyclePlayer(Player):
    def move(self):
        choice_index = 0
        if choice_index < int(len(moves)):
            cp_move = moves[choice_index]
            choice_index += 1
            return cp_move
        else:
            choice_index = 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) == True:
            self.p1.score += 1
            print("Player 1 Wins!")
        elif move1 == move2:
            print("Tie Game!")
        elif beats(move1, move2) != True:
            self.p2.score += 1
            print("Player 2 Wins!")

    def final_score(self):
        print(f"Final score: Player 1 = {self.p1.score} | Player 2 = {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("Player 1 Wins the Best of 3!!")
        elif self.p1.score < self.p2.score:
            print("Player 2 Wins the Best of 3!!")
        else:
            print("Nobody Won the Best of 3.")

    def play_game(self):
        print("Game start!")
        for round in range(7):
            print(f"Round {round}:")
            self.play_round()
        self.final_score()
        print("Game over!")


if __name__ == '__main__':
    game = Game(CyclePlayer(), RandomPlayer())
    game.play_game()
