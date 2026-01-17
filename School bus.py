class vehicle:
    def __init__(self,name,max_speed,mileage,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity*100 

class bus(vehicle):
    def fare(self):
        maintainence = self.capacity*100
        return maintainence+maintainence*0.1
    

obj = bus("Mercedes Bus",150,25,50)
print("Name: ",obj.name,"Max speed: ",obj.max_speed,"Mileage: ",obj.mileage,"Fare: ",obj.fare())