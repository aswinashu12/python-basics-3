class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class car(vehicle):
    def move(self):
        print("Move")
class boat(vehicle):
    def move(self):
        print("sail")
class plane(vehicle):
    def move(self):
        print("fly")
x_car=car("ford","shelby")
x_plane=plane("boeing",747)
x_boat=boat("ibiza","touring 20")
for y in (x_car,x_plane,x_plane):
    print(y.brand)
    print(y.model)
    y.move()
