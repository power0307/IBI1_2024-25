import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary to store the popularity of programming languages
language_popularity = {
    "JavaScript": 62.3,
    "c": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}

# Print the dictionary of language popularity
print(language_popularity)

# Draw a bar graph to visualize the popularity of programming languages and provide some information about the graph
N = 5
# Get the popularity percentage of JavaScript
a = language_popularity["JavaScript"]
# Get the popularity percentage of C
b = language_popularity["c"]
# Get the popularity percentage of Python
c = language_popularity["Python"]
# Get the popularity percentage of SQL
d = language_popularity["SQL"]
# Get the popularity percentage of TypeScript
e = language_popularity["TypeScript"]
# Create a tuple to store the popularity percentages of all languages
Percentage_of_Developers = (a, b, c, d, e)
# Generate an array of evenly spaced values for the x-axis
ind = np.arange(N)
# Set the width of the bars in the bar graph
width = 0.35
# Create the bar graph
p1 = plt.bar(ind, Percentage_of_Developers, width)
# Set the labels for the x-axis
plt.xticks(ind, ("JavaScript", "HTML", "Python", "SQL", "TypeScript"))
# Set the tick values for the y-axis
plt.yticks(np.arange(0, 70, 5))
# Set the label for the y-axis
plt.ylabel("Percentage_of_Developers")
# Set the title of the bar graph
plt.title("Programming Language Popularity (2024)")
# Display the bar graph
plt.show()

# Check the usage rate of a specific language in the dictionary
query_language = "Python"  # You can choose the keys in the dictionary
print(f"{query_language} is used by {language_popularity.get(query_language)}% of developers.")