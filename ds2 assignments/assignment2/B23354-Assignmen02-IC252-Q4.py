import matplotlib.pyplot as plt
import random

data=[]

def throwing_2dice(n):
    for i in range(n):
        a= random.randint(1,6)
        b= random.randint(1,6)
        data.append(a+b)
        probability= [data.count(j)/n for j in range(2,13)]
        frequency =  [data.count(j) for j in range(2,13)] #this is the frequency of each sum
    return probability

plt.bar(range(2,13), throwing_2dice(10000))
plt.ylabel('Probability')
plt.xlabel('Sum of 2 dice')
plt.title('Experiment : Probability of sum of 2 dice after n throws')
plt.savefig('throwing_2dice.png')
plt.show()


    












    