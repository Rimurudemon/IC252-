import numpy as np
import matplotlib.pyplot as plt

def birthday_paradox(k):
    return 1 - np.prod([(365 - i) / 365 for i in range(k)])


k = np.arange(2,101)

probability = [birthday_paradox(i) for i in k]

plt.plot(k, probability)

plt.xlabel('People in the room')
plt.ylabel('Probability of failure of paradox')
plt.title('Birthday paradox')
plt.savefig('birthday_paradox.png')
plt.show()


