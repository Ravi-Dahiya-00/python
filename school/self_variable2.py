class car:
    
    def set_engine_model(self,engine):
        self.engine=engine
        
    
    def get_engine_model(self):
        print(self.engine)


class honda(car):
    
    def set_car_model(self,model):
        self.model=model
        
    def get_car_model(self):
        print(self.model)



my_car = honda()



my_car.set_engine_model("s_model")
my_car.set_car_model(6969)

print("car details : ")

my_car.get_engine_model()
my_car.get_car_model()
