# psedocode:
# get imformation about one person's weight and height
#  𝐵𝑀𝐼 =	w / h**2  
# judge his/her body situation
w = float(input(" Your weight: ")) # get weight
h = float(input(" Your height: ")) # get height
BMI = w / h**2 # caculate
print ("Your BMI is:" + str(BMI)) # print BMI
if BMI < 18.5: # judge
    print("underweight") # light situation
elif 18.5 <= BMI <= 30:
    print("normal weight") # healthy situation
else:
    print("obese") #  fat situation