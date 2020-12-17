import random
 
from bke import *
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    
random.seed(1)
 
my_agent = MyAgent()
random_agent = RandomAgent()
my_agent = MyAgent(alpha=0.8, epsilon=0.2)
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)
