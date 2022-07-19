from ast import Return
import random
from tracemalloc import start
import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissors:
    '''
    A Rock, Paper and Scissors game that captures input from users' image on a webcam and compares it with the Computer's choice.
    A winner is selected based on the rules of the game.
    The game ends when either the User or computer records the highest number of wins out of 5 rounds.
    
    Attributes:
    ----------
    comp_options: list
        List of words that the computer will select randomly from
    computer_choice : string
        A random choice by the computer from the list of game options
    user_choice : string
        The label that corresponds to the index of highest probability from the list of probabilities
    index_max : integer
        Returns the Index of the highest probability
    computer_wins : integer
        Total Number of winnings by the Computer
    user_wins : integer
        Total Number of winnings by the User
    rounds_played : integer
        Number of rounds played in the game

    Methods:
    -------
    get_user_instruction()
        Welcomes Player and displays game Instructions.
    get_user_name()
        Welcomes the User to the game and obtains Name of user.
    get_computer_choice()
        Randomly picks a word from list of game options.
    get_user_choice()
        Obtains User choice from the probability predicted.
    get_prediction()
        Predicts the probablities of each class of the model from user input.
    get_round_winner()
        Compares user choice with computer choice and decides the winner of the round based on the game rules.
    get_overall_winner
        The player with the highest number of rounds won, wins the game
    close_window
        This closes the Cap and destroy all windows
    '''
    def __init__(self):
        self.comp_options = ["Rock", "Paper", "Scissors"]
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds_played = 0
        self.user_choice = ""
        self.computer_choice = ""
        self.cap = cv2.VideoCapture(0)
        self.user_name = "" 

    # Welcomes Player and displays game Instructions     
    def get_user_instruction(self):
        print("")
        print("Welcome to an Interactive Rock, Paper and Scissors game developed by Tiwalade")
        print("**=========================================================================**")
        print ("")
        print("Game Instructions!!!")
        print ("")
        print("You will play this game for 5 rounds.")
        print("You will show your choice to the camera on the webcam display and press 'c' to capture your image.")
        print("A winner is decided on each round.")
        print("The overall winner is the player with the highest number of wins after the 5th round")
        print("      _               _ ___, _      _      _       ")
        print("|\ | | | |  |    |   |_  |  |_     |_| |  |_| |_|  ")
        print("| \| |_| |/\|    |__ |_  |   _|    |   |_ | |   |  ")
        print("")

    # Obtains Player's Name
    def get_user_name(self):
        while True:
            self.user_name = input("Please Enter your Name: ")       
            if len(self.user_name) > 0:
                print(f" Welcome {self.user_name}!, Now please show your choice to the camera on the next screen and press 'c' to capture it.")
                print("")
                return self.user_name
            else:
                print ("Please, enter at least a character to begin!")
        
        

    # Gets computer's random choice between Rock, Paper or Scissors
    def get_computer_choice(self):                          
        self.computer_choice = random.choice(self.comp_options)
        return self.computer_choice

    # Maps the prediction from camera input to the corresponding class label 
    def get_user_choice(self):
        index_max  = np.argmax(self.prediction)
        if index_max == 0:
            self.user_choice = "Rock" 
        elif index_max == 1:
            self.user_choice = "Paper" 
        elif index_max == 2:
            self.user_choice = "Scissors"
        else:
            self.user_choice = "Nothing"
            return self.user_choice

    # Predicts the probablities of each class of the model from camera input
    def get_prediction(self):               
        model = load_model('keras_model.h5')   
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        while time.time() < time.time() + 100:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_CUBIC)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            self.prediction = model.predict(data)
            cv2.imshow ('frame', frame)                  
            print(f"{self.prediction}")
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break
        return self.prediction
        
    # Methods puts the game rules in place to check the winner of each round
    def get_round_winner(self):             
            if (self.user_choice == "Rock" and self.computer_choice == "Scissors") or (self.user_choice == "Paper" and self.computer_choice == "Rock") or (self.user_choice == "Scissors" and self.computer_choice == "Paper"):
                self.rounds_played += 1 
                print("")
                print(f" Round {self.rounds_played}")
                print(" =======")
                print(f" {self.user_name}'s choice: {self.user_choice}")
                print(f" Computer's choice: {self.computer_choice}")
                winner = self.user_name             
                self.user_wins += 1 
                print(f" Round winner: {winner}")
                print("")
            elif (self.user_choice == "Rock" and self.computer_choice == "Paper") or (self.user_choice == "Paper" and self.computer_choice == "Scissors") or (self.user_choice == "Scissors" and self.computer_choice == "Rock"):
                self.rounds_played += 1 
                print("")
                print(f" Round {self.rounds_played}")
                print(" =======")
                print(f" {self.user_name}'s choice: {self.user_choice}")
                print(f" Computer's choice: {self.computer_choice}")
                winner = "Computer"
                self.computer_wins += 1
                print(f" Round winner: {winner}")
                print("")
            elif (self.user_choice == "Nothing" and self.computer_choice == "Paper") or (self.user_choice == "Nothing" and self.computer_choice == "Scissors") or (self.user_choice == "Nothing" and self.computer_choice == "Rock"):
                self.rounds_played += 1 
                print("")
                print(f" Round {self.rounds_played}")
                print(" =======")
                print(f" {self.user_name}'s choice: {self.user_choice} ")
                print(f" Computer's choice: {self.computer_choice}")
                winner = "Computer"
                self.computer_wins += 1
                print(f" Round winner: {winner}")
                print("") 
            else:
                self.rounds_played += 1 
                print("")
                print(f" Round {self.rounds_played}")
                print(" =======")
                print(f" {self.user_name}'s choice: {self.user_choice} ")
                print(f" Computer's choice: {self.computer_choice}")
                winner = "Tie - No winner"               
                print(f" Round winner: {winner}")
                print("")  

    # Determines the overall winner after 5 Rounds
    def get_overall_winner(self):               
        if self.rounds_played == 5 :        
            if self.computer_wins > self.user_wins:
                print("")
                print (f" Final Scores :  Computer : {self.computer_wins}")
                print (f"                    {self.user_name}: {self.user_wins}")
                print (f" Computer Won!!!")
            elif self.user_wins > self.computer_wins:
                print("")
                print (f" Final Scores :  Computer : {self.computer_wins}") 
                print (f"                     {self.user_name}: {self.user_wins}")
                print (f" Amazing! {self.user_name} Won!!!")
            else:
                print("")
                print (f" Final Scores :  Computer : {self.computer_wins}") 
                print (f"                            {self.user_name}: {self.user_wins}")
                print (f" No Overall Winner!!!")
                return

    # Shutdown the camera   
    def close_window(self):
        self.cap.release()                      
        cv2.destroyAllWindows() 

# Defines a function that creates an instance of the Class . 
def play():                                    
    beginplay = RockPaperScissors()       # Creates an instance of the Class
    beginplay.get_user_instruction()             
    beginplay.get_user_name()
    while beginplay.rounds_played < 5 :
        beginplay.get_computer_choice()
        beginplay.get_prediction()
        beginplay.get_user_choice()
        beginplay.get_round_winner()
        beginplay.get_overall_winner()
    beginplay.close_window    
                         
                    
        
    
#Calls the play function to begin the game
play()                                            

# %%
