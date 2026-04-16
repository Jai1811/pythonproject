class Car:

    car_type = "car type 1"
    car_type_class = "car type class 1"

    # static method these do not either change or access class or instance attributes
    @staticmethod
    def car_start():
        print("Car started...")
    @staticmethod
    def car_stopped():
        print("car stopped")

    #instance methods having self as an argument these belong to objects having
    def changeCarType(self, car_type, car_type_class):
        self.car_type = car_type
        Car.car_type_class = car_type_class

    #class methods having cls as an argument these belong to the class
    @classmethod
    def changeClassAttributes(cls, car_type):
        cls.car_type = car_type

class BMW(Car) :

        def __init__(self, brand, type):
            self.brand = brand
            self.type = type


class BMWX1(BMW) :
    def __init__(self, variant, type):
        super().__init__(brand="BMW", type=type)
        self.variant = variant



class DSG(BMWX1):

    def __init__(self, chassis, variant, fuelTankSize):
        super().__init__(variant=variant,type="DSG automatic")
        super().car_start()
        self.chassis = chassis
        self.fuelTankSize = fuelTankSize

    @property
    def fullTankSize(self):
        return 2 * self.fuelTankSize


car = Car()
car.changeCarType("Car type 121234","Car type class 12132")
print(car.car_type,",",Car.car_type_class)
print(Car.car_type)

car1 = BMWX1("petrol","DSG Automatic")
print(car1.variant)

car2 = DSG("21312425ajkxdfbasdf","desiel",56)
print(car2.fullTankSize)
