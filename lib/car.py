from vehicle import Vehicle
import ipdb

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

guido = Car(11, 14)
ipdb.set_trace()