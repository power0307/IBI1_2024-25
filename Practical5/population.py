
import matplotlib.pyplot as plt
# 2. 人口规模
# UK 国家人口数据
uk_countries = {
    "England": 57.11,
    "Wales": 3.13,
    "Northern Ireland": 1.91,
    "Scotland": 5.45
}

# 浙江邻近省份人口数据
china_provinces = {
    "Zhejiang": 65.77,
    "Fujian": 41.88,
    "Jiangxi": 45.28,
    "Anhui": 61.27,
    "Jiangsu": 85.15
}

# 排序并打印
sorted_uk = sorted(uk_countries.items(), key=lambda x: x[1])
sorted_china = sorted(china_provinces.items(), key=lambda x: x[1])
print("Sorted UK Population:", sorted_uk)
print("Sorted China Population:", sorted_china)

# 绘制 UK 人口和中国省份人口饼图在同一张图上
fig, axes = plt.subplots(1, 2, figsize=(12,6))

# UK 人口饼图
axes[0].pie(uk_countries.values(), labels=uk_countries.keys(), autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
axes[0].set_title("Population Distribution in UK (2022)")

# 中国省份人口饼图
axes[1].pie(china_provinces.values(), labels=china_provinces.keys(), autopct='%1.1f%%', colors=['orange', 'pink', 'cyan', 'yellow', 'brown'])
axes[1].set_title("Population Distribution in Zhejiang Neighboring Provinces (2022)")

plt.show()
