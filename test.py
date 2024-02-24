
import numpy as np  
import matplotlib.pyplot as plt
import math
import random

data=[]
def game(b):
    s=[]
    d= [i for i in range(1,b+1)]
    for j in range(1,b+1):
        a= random.choice(d)
        d.remove(a)
        if j==a:
            s.append(1)
            break
    if len(s)==0:
            return(0)
    else:
        return(s)

probabilities = []

for b in range(2, 21):  # Number of boxes from 2 to 20
    for _ in range(50):  # Repeat the experiment 50 times
        data.append(game(b))
    losses = data.count(0)
    wins = 50 - losses
    probabilities.append(wins / 50)
    data = []



box_numbers = list(range(2, 21))

plt.plot(box_numbers, probabilities)
plt.xlabel('Number of cards')
plt.ylabel('Probability of Winning')
plt.title('Probability of Winning vs. Number of cards')
plt.grid(True)
plt.show()

# b=3
   
# for i in range(50):
#     data.append(game(b))

# l= data.count(0)

# w= 50-l
# print(f'probability of winning is {w/50} and probability of losing is {l/50}')

# plt.hist(data, bins=20, color='c', edgecolor='black')
# plt.show()


