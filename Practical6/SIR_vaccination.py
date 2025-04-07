import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
beta = 0.3 # set beta and gamma value
gamma = 0.05
N = 5000
infected_init = 1 # set empty value
recover_init = 0
vaccine = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] #list vaccine propotion from 0 to 1

plt.figure(figsize=(6, 4), dpi=150)

for i, vac_rate in enumerate(vaccine): # check the index and value one by one
    if i == 10: # all people get vaccination
        I_list = [0]
        plt.plot (I_list , color=cm. viridis (i*25), label=f'Vaccine rate: {100.0}%')
        break
    elif i <= 9: # basic information about people
        infected = infected_init
        recover = recover_init
        susceptible = N - infected - int(vac_rate * N)
        S_list = [susceptible]
        R_list = [recover]
        I_list = [infected]

        for time in range(1000): # run 1000 times
            pro = float(beta * infected / N) # the probality of infection
            new_infected = np.random.choice(range(2), int(susceptible), p=[1 - pro, pro])
            new_recover = np.random.choice(range(2), infected, p=[1 - gamma, gamma])
            infected = infected + np.sum(new_infected) - np.sum(new_recover)
            recover = recover + np.sum(new_recover)
            susceptible = susceptible - np.sum(new_infected)
            S_list.append(susceptible)
            R_list.append(recover)
            I_list.append(infected)

    plt.plot (I_list , color=cm. viridis (i*25), label=f'Vaccine rate: {vac_rate * 100}%')
plt.xticks(np.arange(0, 1001, 200))
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig("SIR_model.png", format="png")
plt.show()
    