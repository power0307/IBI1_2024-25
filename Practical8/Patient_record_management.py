class patients():
    def __init__(self,name,age,date_of_latest_admission,medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medica_history = medical_history
    def inforation(self):
        print(self.name,self.age,self.date_of_latest_admission,self.medica_history)
c = patients("a",13,2001,"no")
patients.inforation(c)