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
    
 
my_agent = MyAgent()
validation_agent = RandomAgent()
my_agent = MyAgent(alpha=0.5, epsilon=0.07)
 
train(my_agent, 4000)

validation_result = validate(
    agent_x=my_agent,
    agent_o=validation_agent,
    iterations=50,)

plot_validation(validation_result)
