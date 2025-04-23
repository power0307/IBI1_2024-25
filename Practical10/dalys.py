import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\F\Desktop\IBI1\IBI1_2024-25\Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

b = dalys_data.iloc[0:10,2] # the third column (Year) for the first 10 rows(the 10th year is 1999)
print(b) # print it

a = dalys_data.loc[dalys_data.Year==1990, ["DALYs"]] # DALYs for all countries in 1990
print(a)# print it

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]] # Select rows from the dalys_data where the 'Entity' column is equal to "United Kingdom",and select the 'DALYs' and 'Year' columns.
france = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]] # Select rows from the dalys_data where the 'Entity' column is equal to "France",and select the 'DALYs' and 'Year' columns.
desc_uk = uk['DALYs'].describe() # Generate descriptive statistics for the 'DALYs' column in uk
desc_france = france['DALYs'].describe() # Generate descriptive statistics for the 'DALYs' column in france
uk_mean = desc_uk["mean"] # Get the mean value
france_mean = desc_france["mean"] # Get the mean value

if uk_mean > france_mean: # compare the values and print the country with the larger value
    print("UK's mean is larger") #UK's mean is larger in fact
else:
    print("France's mean is larger")

uk_std = desc_uk["std"] # Get the standard deviation value
france_std = desc_france["std"] # Get the standard deviation value
if uk_std > france_std: # compare the values and print the country with the larger value
    print("UK's standard deviation is larger") #France's standard deviation is larger in fact
else:
    print("France's standard deviation is larger")

plt.plot(uk.Year, uk.DALYs, 'r+') # marked with red plus signs.
plt.xticks(uk.Year,rotation=-90) # Set the x - axis ticks to the 'Year' column of uk and rotate the tick labels by -90 degrees.
plt.show() # Display the plotted image