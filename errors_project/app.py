class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise ValueError(f'Tried to add `{car.__class__.__name__}`to the garage, but you can only add Car objects')
        self.cars.append(car)


ford = Garage()

fiesta = Car('ford', 'fiesta')
try:
    ford.add_car(fiesta)
except TypeError:
    print("Your car is not a car")
except ValueError:
    print("Something strange happened")
finally: print(f'The garage now has {len(ford)} cars')
print((ford))
