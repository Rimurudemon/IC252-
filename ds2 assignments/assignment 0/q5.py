
###Create a subplot with two plots side by side. Plot a sine wave in the first subplot. Plot a cosine wave in the
#second subplot. Add labels, titles, and a legend to the plots.
import numpy as np
import matplotlib.pyplot as plt

steps= 0.1
x = np.arange(-5,5,steps)
y1 = np.sin(x)
y2 = np.cos(x)
fig, axs = plt.subplots(1, 2)
axs[0].plot(x, y1, color='red', label='sine wave')
axs[0].set_title('Sine Wave')
axs[0].set_xlabel('values of x')
axs[0].set_ylabel('output of function')
axs[0].grid()
axs[1].plot(x, y2, color='blue')
axs[1].set_title('Cosine Wave')
axs[1].set_xlabel('values of x')
axs[1].set_ylabel('output of function')
axs[1].grid()
plt.show()


