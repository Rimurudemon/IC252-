import numpy as np
import matplotlib.pyplot as plt


def game_prob(n):
    s=0
    for i in range(1,n+1):
        s+=((-1)**(i+1))/(np.math.factorial(i))  #dearrangement 
    return s
#print(check_prob(4))
k=list(range(1,101))
prob=[game_prob(i) for i in k]
plt.plot(k,prob)

plt.xlabel('no. of cards')
plt.ylabel('probability of winning')
plt.title('DE Montmort Matching Problem')
# plt.savefig('de_montmort.png')
plt.show()



print(k[prob.index(max(prob))])




#additional reasearch on the same problem was done using the following link: 
# https://math.stackexchange.com/questions/3320522/de-montmorts-matching-problem-strategy