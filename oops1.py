#initiate a class
class employee:
    #special method/magic method/ dunder method- constructor
    def __init__(self):
        self.name="username"
        print(id(self))
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
print(sam.id)
sam.name="sameer"
print(sam.name)
#calling a method
print(id(sam))
print(type(sam))
sam.travel("kerala")   #self as the first parameter.if you wwant to use kerala as paramter , then define two parameter in method