**COMPUTER VISION PROJECT DOCUMENTATION GUIDELINE**

A computer Rock Paper Scissors game that predicts Rock, paper or scissors based on the Image shown to the computer screen.

**MILESTONE 1**

An image model is created with four classes: Rock, Paper, Scissors and Nothing. The model is trained on the "Teachable machine" by showing several images of myself showing each option to the camera.

**MILESTONE 2**

The trained model named keras_model.h5 is downloaded along with the labels (labels.txt) and pushed to the GitHub repository.

**MILESTONE 3**
Here, different functions are created to handle different tasks.
The get_computer_choice function helps the computer to select a random choice from the 3 options available - Rock, Paper or Scissors
The get_user_choice asks for an input from the user. 
The get_winner functions does a comparison of inputs of the User and the Computer, and annouces a winner based on the rules of the game.
The Play function actually plays the game. It calls the previous functions into play.
