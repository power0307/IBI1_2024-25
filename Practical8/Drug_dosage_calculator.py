def Drug_dosage_calculator(weight,strength): # def a function
    if weight <=10 or weight >=100: # report an error if the weight is out of range
        print(" your weight is wrong")
        return
    if strength == "120mg/5ml": # replace the string with value
       s = 24
    elif strength == "120mg/5ml":
       s = 50
    else: # report an error if the strength of paracetamol is wrong
        print(" your strength of paracetamol is wrong")
        return
    dose = float(weight/s) # calculate the dose
    print(dose,"ml")
    return
Drug_dosage_calculator(45,"120mg/5ml")
