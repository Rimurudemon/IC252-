import random
import matplotlib.pyplot as plt

def monty_hall(n):
    win_with_switch=0
    win_without_switch=0
    for i in range(n):
        doors= [0,0,1]
        random.shuffle(doors)
        #b=int(input('Enter your choice of door 1, 2 or 3:'))-1  ----------->for simulating using manual input
        player_choice= random.randint(0, 2)
        #goat reveal
        monty_options = [i for i in range(3) if i != player_choice and doors[i] == 0]
        monty_choice = random.choice(monty_options)  # this is the door monty opens
    
        other_door = [i for i in range(3) if i != player_choice and i != monty_choice][0] #this is the door the player can switch to
        
        # Count wins
        if doors[player_choice] == 1:
            win_without_switch += 1
        else:
            win_with_switch += 1
    return win_without_switch/n, win_with_switch/n

print(monty_hall(10000))
plt.bar(['Without Switch','With Switch'],monty_hall(10000))
plt.ylabel('Probability of winning')
plt.title('Monty Hall Problem')
plt.savefig('monty_hall.png')
plt.show()

