class employee:
    def __init__(self):
       self.id = 123
       self.salary = 30000
       self.designation = "SDE"

    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")


sam = employee()

sam.travel("kerala")   
