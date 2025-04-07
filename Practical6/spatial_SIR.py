import numpy as np
import matplotlib.pyplot as plt

# Initialize the population matrix
population = np.zeros((100, 100))

# Select an initial infection point at random
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# Define infection rates and recovery rates
beta = 0.3
gamma = 0.05

for time in range(0, 101):
    # Find an index of infected and recovered points
    infectedIndex = np.where(population == 1)
    recoverIndex = np.where(population == 2)

    # Spread process
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in range(x - 1, x + 2): # the infection area
            for yNeighbour in range(y - 1, y + 2):
                if (xNeighbour, yNeighbour) != (x, y):
                    if xNeighbour != 2 and yNeighbour != 2 and xNeighbour!=100 and yNeighbour!=100: # the recover anf edge aren't infected
                        if population[xNeighbour, yNeighbour] == 0:
                            population[xNeighbour, yNeighbour] = np.random.choice(range(2), 1, p=[1 - beta, beta])[0]

    # Recovery situation
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        if np.random.choice(range(2), 1, p=[1 - gamma, gamma])[0] == 1:
            population[x, y] = 2

    # Draw at a specific point in time
    if time in [0, 10, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap="viridis", interpolation="nearest")
        plt.show()
    