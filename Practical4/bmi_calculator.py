# psedocode:
# get imformation about one person's weight and height
#  𝐵𝑀𝐼 =	w / h**2  
# judge his/her body situation
w = float(input(" Your weight: ")) # get weight
h = float(input(" Your height: ")) # get height
BMI = w / h**2 # caculate
if BMI < 18.5: # judge
    print(" too light") # too light situation
elif 18.5 <= BMI < 24:
    print("healthy") # healthy situation
elif 24 <= BMI < 28:
    print("fat") # fat situation
else:
    print("too fat") # too fat situation