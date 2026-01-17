class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    pass

obj = bus("Mercedes Bus",150,25)
print("Name: ",obj.name,"Max speed: ",obj.max_speed,"Mileage: ",obj.mileage)