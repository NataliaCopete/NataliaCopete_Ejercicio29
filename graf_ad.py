import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
delta_x=0.05;
L = 4.0
N = int(L/delta_x + 1)
data=np.loadtxt("advecc.txt")
plt.plot(data[0:81,1],data[0:81,0],label="iniciales")
for i in range(1,5):
    plt.plot(data[i*(N+1):(i+1)*(N+1),1],data[i*(N+1):(i+1)*(N+1),0], label=str((i-1)*0.5))
    plt.legend()
plt.ylim((0.0,1.2))
plt.savefig("adveccion.pdf")
