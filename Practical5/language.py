import numpy as np
import matplotlib.pyplot as plt

# create dictionary
language_popularity = {
    "JavaScript": 62.3,
    "c": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}

# print dictionary
print(language_popularity)

# draw the bar graph and give some information about the bar graph
N = 5
a = 62.3
b = 52.9
c = 51
d = 51
e = 38.5
Percentage_of_Developers = (a,b,c,d,e)
ind = np.arange(N)
width = 0.35
p1 = plt.bar(ind, Percentage_of_Developers, width)
plt.xticks(ind, ("JavaScript","HTML","Python","SQL","TypeScript"))
plt.yticks(np.arange(0,70,5))
plt.ylabel("Percentage_of_Developers")
plt.title("Programming Language Popularity (2024)")
plt.show()

# check the usage rate of languages in the dictionary
query_language = "Python"  # you can choose the keys in the dictionary
print(f"{query_language} is used by {language_popularity.get(query_language)}% of developers.")