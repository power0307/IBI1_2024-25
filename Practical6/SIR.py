import numpy as np
import matplotlib.pyplot as plt

beta = 0.3 # set beta and gamma value
gamma = 0.05
N = 10000
infected = 1 # set empty value
recover = 0
susceptible = N - 1
S_list = [susceptible] #set lists
R_list = [recover]
I_list = [infected]

for time in range(1000):
    pro = float(beta * infected / N) # infection probality
    new_infected = np.random.choice(range(2), susceptible, p=[1 - pro, pro]) # random infection 
    new_recover = np.random.choice(range(2), infected, p=[1 - gamma, gamma]) # random recovery
    infected = infected + np.sum(new_infected) - np.sum(new_recover) # new infection
    recover = recover + np.sum(new_recover) # new recovery
    susceptible = susceptible - np.sum(new_infected) # new susceptible
    S_list.append(susceptible) # change lists
    R_list.append(recover)
    I_list.append(infected)

plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='susceptible', color="blue")
plt.plot(I_list, label='infected', color="orange")
plt.plot(R_list, label='recovered', color="green")
plt.xticks(np.arange(0, 1001, 200))
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.savefig("SIR_model.png", format="png")
plt.show()