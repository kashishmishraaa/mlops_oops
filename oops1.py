#initiate a class
class employee:
    #special method/magic method/ dunder method- constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id=123
        self.salary=75000
        self.designation="SDE"
        print("attributes/data have been initiated")
    #method/function
    def travel(self,destination):
        print("this travel function was called manually")
        print(f"employee is now travelling to {destination}")
#create an object of the class
sam=employee()
#print(sam.id)
#calling a method
#sam.travel("kerala")
print(type(sam))