**COMPUTER VISION PROJECT DOCUMENTATION GUIDELINE**

A computer Rock Paper Scissors game that predicts Rock, Paper or Scissors based on the Image shown to the computer screen.

**MILESTONE 1**

An image model is created with four classes: Rock, Paper, Scissors and Nothing. The model is trained on the "Teachable machine" by showing several images of myself showing each option to the camera.

**MILESTONE 2**

The trained model named keras_model.h5 is downloaded along with its labels. (labels.txt)

Before the model was used, the depenencies that it needed to run was installed.

It started by creating a virtual environment(rps_env), activated it, installed pip and every other libraries - opencv, tensorflow, ipykernel etc

**MILESTONE 3**

Here, the Rock paper scsissors game is created to be played manually by each user typing their choice.

Different funtions were created to handle different tasks.

The get_computer_choice function helps the computer to select a random choice from the 3 options available - Rock, Paper or Scissors.

The get_user_choice asks for an input from the user.

The get_winner functions does a comparison of inputs of the User and the Computer, and annouces a winner based on the rules of the game.

The Play function actually plays the game. It calls the previous functions into play.

This code is in manual_rps python file

**MILESTONE 4**

The camera (webcam display) is used to play the game. The script is located in camera_rps.py

The manual input is replaced by the user choice shown to the camera. 

Object oriented programming is used to handle all the tasks in this milestone.

A Class (RockPaperScissoors) is defined with all attributes as shown in the init method shown below: 

![image](https://user-images.githubusercontent.com/108297261/179721133-728addf0-dada-4cb2-a940-5c785e695667.png)

 and methods to be used in the class as well:
 
 ![image](https://user-images.githubusercontent.com/108297261/179724007-ea2b79e8-e812-412d-9ad4-11139d971b27.png)
 
 The Computer makes its choice by selecting at random between Rock,Paper or Scissors using the get_computer_choice method
 
 ![image](https://user-images.githubusercontent.com/108297261/179727948-ee219a55-9e37-4c5e-9a47-a6529baa8247.png)


Method get_prediction is used to get the output of the model we downloaded earlier as shown below: 

![image](https://user-images.githubusercontent.com/108297261/179722779-1a7e0810-ec7f-4f4a-8327-d5b9de624503.png)

The script reads input from the camera every 100 seconds since the last input. This was done by implementing Function time.time() + 100.

When a user shows their choice to the camera, the model captures the input and predicts a list of probabilities for each class. To know th user input, we pick the class with the highest probability as shown in the get_user_choice method shown below:

![image](https://user-images.githubusercontent.com/108297261/179727508-e8c21e4b-cb73-4e32-ad20-3359b16490b8.png)


The get_round_winner methods puts the game rules in place to check the winner of each round. The winner of each round is stored in varaiables user_wins or computer_wins which increases every round depending on the winner of the round. No_rounds_played is a counter that also increases each time a round is played.

Method get_overall_winner determines the overall winner after 5 rounds:

The player with the higher number of wins after 5 rounds wins the game

![image](https://user-images.githubusercontent.com/108297261/179725462-a9bbc859-49db-4e86-9aa2-45b71f1593cc.png)

The game is played by defining a function to create an instance of the class and calling the function.


The game begins by displaying a set of instruction the the user, thereafter requests for the player's name before the game begins.

![image](https://user-images.githubusercontent.com/108297261/179730034-3412069b-795a-4a58-b674-9f29dd2da2bc.png)


The game can be improved by having the round wins and overall winner displayed on the Web display.






