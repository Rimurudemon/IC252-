import numpy  as np
import matplotlib.pyplot as plt

def f(n):
    if n == 0:
        return 1
    return np.math.factorial(n)/(np.sqrt(2 * np.pi * n) * (n / np.e) ** n)

x= np.arange(1, 20, 1)

plt.plot(x,[f(i) for i in x])
plt.ylabel('Stirling approximation')
plt.title('Demonstration of Stirling approximation for n!')
plt.xlabel('n')
# plt.savefig('stirling.png')
plt.show()

