import random as random


class GuessTheNumber:
    def guess(self,a,b):
        if User_input == computer:
            return "You Won!"

        
        else:
            return "You Lost!"
 



User_input = int(input("Enter your guess number beetween 1,100: ")) 
computer = random.randint(1,100)
game = GuessTheNumber()
result = game.guess(User_input,computer)
print(result)


