import matplotlib.pyplot as plt
# UK population data
uk_countries = {
    "England": 57.11,
    "Wales": 3.13,
    "Northern Ireland": 1.91,
    "Scotland": 5.45
}

# the provinces in China which border Zhejiang province population data
china_provinces = {
    "Zhejiang": 65.77,
    "Fujian": 41.88,
    "Jiangxi": 45.28,
    "Anhui": 61.27,
    "Jiangsu": 85.15
}

# sort two dictionaries and print them from bigger to smaller separately
sorted_uk = sorted(uk_countries.items(), key=lambda x: x[1], reverse = True)
sorted_china = sorted(china_provinces.items(), key=lambda x: x[1], reverse = True)
print("Sorted UK Population:", sorted_uk)
print("Sorted China Population:", sorted_china)

# Plot the pie charts of the UK population and the population of Chinese provinces on the same chart.

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# UK population pie chart
axes[0].pie(uk_countries.values(), labels=uk_countries.keys(), autopct='%1.1f%%', colors=['pink', 'green', 'red', 'purple'])
axes[0].set_title("Population Distribution in UK (2022)")

# China provinces population pie chart
axes[1].pie(china_provinces.values(), labels=china_provinces.keys(), autopct='%1.1f%%', colors=['orange', 'pink', 'cyan', 'yellow', 'brown'])
axes[1].set_title("Population Distribution in Zhejiang Neighboring Provinces (2022)")

plt.show()
