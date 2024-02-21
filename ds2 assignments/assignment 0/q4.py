import numpy as np
import matplotlib.pyplot as plt

def f(x:np.ndarray)->np.ndarray:
  return ((np.sin(x))**7+(np.cos(x))**5)/np.exp(x)
pass

steps= 1000
x = x= np.arange(0,4, 1/steps)
y = f(x)
plt.xlabel('values of x')
plt.ylabel('output of function')
plt.title('Graph of function')  
plt.grid()  
plt.plot(x, y, color='red')
plt.show()