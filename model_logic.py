# DDQN Architecture Sample for Autonomous Driving
# Demonstrates the Neural Network used to process 'Ray-cast' sensor data

import torch
import torch.nn as nn
import torch.nn.functional as F

class DDQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DDQN, self).__init__()
        # Input: Distances from the 5-7 'imaginary lines' (sensors)
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        # Output: Q-values for actions (Left, Right, Straight)
        self.fc3 = nn.Linear(64, action_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)

# Logic Note:
# The 'Double' in DDQN comes from using two networks: 
# One to choose the action and one to evaluate the action,
# preventing the car from becoming 'overconfident' in bad moves.
