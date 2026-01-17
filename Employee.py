class person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post=post
        super().__init__(name,idnumber)

obj = employee("Nikhil",12345,5000,"intern")
obj.display()