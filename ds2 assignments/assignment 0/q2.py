import matplotlib . pyplot as plt
import numpy as np
np.random.seed(0)
val = np . random . normal ( size =(100) , scale =3 , loc =10)
bins =np. arange (0 ,30 ,1)
plt . hist ( val , bins =bins,edgecolor='black',color='yellow',alpha=0.7,linewidth=2,hatch='.')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt . show ()
# fig, axs = plt.subplots(1, 1,
#                         figsize =(10, 7), 
#                         tight_layout = True)
# axs.xaxis.set_tick_params(pad = 5) 
# axs.yaxis.set_tick_params(pad = 10)

