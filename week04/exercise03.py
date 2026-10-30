#Rock Paper Scissors Game

#Import libraries
import random

class Game:

    #Get human choice
    def Human_choice(self):
        while True:
            #RPS entry + validation
            try:
                human = input(f"Enter Rock, Paper, or Scissors: ").strip()
                if human.lower() != "rock" and human.lower() != "paper" and human.lower() != "scissors":
                    raise ValueError(f"Please enter Rock, Paper, or Scissors")
                break
            except ValueError as error:
                print(error)

        return human

    #Generate computer choice
    def Computer_choice(self):
        computer = random.choice(["rock", "paper", "scissors"])
        return computer

    def Game_winner(self, human, computer):

        #Print win/lose/tie results
        if human.lower() == computer:
            return "It's a tie!"
        elif human.lower() == "rock" and computer == "scissors":
            return "Oh yeah! Human wins :)"
        elif human.lower() == "rock" and computer == "paper":
            return "Oh no! Computer wins :("
        elif human.lower() == "paper" and computer == "rock":
            return "Oh yeah! Human wins :)"
        elif human.lower() == "paper" and computer == "scissors":
            return "Oh no! Computer wins :("
        elif human.lower() == "scissors" and computer == "paper":
            return "Oh yeah! Human wins :)"
        elif human.lower() == "scissors" and computer == "rock":
            return "Oh no! Computer wins :("

    def Play(self):
        while True:

            #Play a round
            human = self.Human_choice()
            computer = self.Computer_choice()
            print(self.Game_winner(human, computer))

            #Print the choices
            print(f"Human entered: '{human.lower()}' and computer chose: '{computer}'")
            
            while True:
                #again entry + validation
                try:
                    again = input(f"Would you like to play again? (Y/N) ").strip()
                    if again.lower() != "n" and again.lower() != "y":
                        raise ValueError(f"Please enter Y or N")
                    break
                except ValueError as error:
                    print(error)

            #Stop if don't continue to play
            if again.lower() == 'n':
                print("Thanks for playing!")
                break

#Create game object
gameObj = Game()
gameObj.Play()