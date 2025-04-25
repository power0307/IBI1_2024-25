# 4.1 Some simple math
a = 15 # walk to bus station
b = 75 # bus runing time
c = a + b # totle time of bus
d = 90 # car running time
e = 5 # walk from the park
f = d + e # totle time of car
if c > f: # compare the totle times
    print ("car is faster")
else:
    print ("bus is faster")
# result: bus is quicker

# 4.2 Booleans
# make list for bool values of x and y
x_values = [False, True]
y_values = [False, True]

# Traverse all possible combinations of X and Y
for X in x_values:
    for Y in y_values:
        # Calculation logic and operation results
        W = X and Y
        # print outcomes
        print(f"if X = {X} and Y = {Y}, then W = {W}")
    
# Table 
# Value_1 |  Value_2 |  Output
#  True   |   True   |   True
#  True   |   False  |   False
#  False  |   True   |   False
#  False  |   False  |   False