class patients():
    def __init__(self,name,age,date_of_latest_admission,medical_history): # give basic information
        self.name = name # the self name
        self.age = age # the self age
        self.date_of_latest_admission = date_of_latest_admission # the self date_of_latest_admission
        self.medica_history = medical_history # the self medical_history
    def inforation(self):
        print(self.name,self.age,self.date_of_latest_admission,self.medica_history)
c = patients("Peter",13,2001,"no") # set an example
patients.inforation(c) # use the function