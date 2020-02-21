import numpy as np
import matplotlib.pyplot as plt

A_1, B_1, C_1, E_1, p0_1, N_1 = 100, 4, 10, 3, 10, 21
P_1 = np.zeros(N_1)
S_1 = np.zeros(N_1)
P_1[0] = p0_1
S_1[1] = 40
for i in range (1, N_1):
    P_1[i] = (A_1 - S_1[i])/B_1
    if i !=N_1 - 1:
        S_1[i+1] = C_1 + E_1*P_1[i]

A_2, B_2, C_2, E_2, p0_2, r_2, N_2 = 100, 3, 5, 3.2, 10, 0.5, 21
P_2 = np.zeros(N_2)
S_2 = np.zeros(N_2)
P_2[0] = p0_2
S_2[0] = C_2 + E_2 * p0_2
for i in range (1, N_2):
    P_2[i] = (A_2 - S_2[i])/B_2
    if i !=N_2 - 1:
        S_2[i+1] = C_2 + E_2*((1-r_2)*P_2[i]+r_2*P_2[i-1])
plt.figure()
plt.plot(P_1, color = 'blue')
plt.plot(P_2, color = 'red')
plt.xlabel('N_кол-во')
plt.ylabel('P_цена')
plt.grid('True')
plt.show()