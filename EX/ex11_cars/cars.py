"""Cars."""

import json


class Car:
    """Car class."""
    fuel_consumption: float

    def __init__(self, make: str, model: str, fuel_consumption: float, features: list[str]):
        """
        Initialize a Car object.

        :param make: The make of the car.
        :param model: The model of the car.
        :param fuel_consumption: The fuel consumption of the car in liters per 100 kilometers.
        :param features: The features of the car.
        """
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.features = features

    def __eq__(self, other):
        """Check if two cars are equal. Don't change this method."""
        return type(other) is self.__class__ and \
            self.make == other.make and \
            self.model == other.model and \
            self.fuel_consumption == other.fuel_consumption and \
            self.features == other.features

    def __hash__(self) -> int:
        """Allow a Car object to be used as a key in a dictionary. Don't change this method."""
        return hash((self.make, self.model, self.fuel_consumption, tuple(self.features)))

    def __repr__(self) -> str:
        """Return a string representation of the Car object. It is not necessary to change this method."""
        return f'{self.make} {self.model}'


def sort_cars_by_make(cars: list[Car]) -> list[Car]:
    """
    Sort the given list of cars by make alphabetically.

    If multiple cars have the same make, sort them by model alphabetically.
    If those cars also have the same model, then the order of those cars doesn't matter.

    :param cars: The list of cars to sort.
    :return: The sorted list of cars.
    """
    return sorted(cars, key = lambda x: (x.make, x.model))



def find_cars_by_make_and_model(cars: list[Car], make: str, model: str) -> list[Car]:
    """
    Find all cars with the given make and model. The order of the cars in the returned list does not matter.

    :param cars: The list of cars to search through.
    :param make: The given make.
    :param model: The given model.
    :return: The list of cars with the given make and model.
    """
    cars_with_make_and_model = []
    for car in cars:
        if car.make == make and car.model == model:
            cars_with_make_and_model.append(car)
    return cars_with_make_and_model


def find_cars_by_feature(cars: list[Car], feature: str) -> list[Car]:
    """
    Find all cars that have the given feature.

    Sort the resulting list of cars by make alphabetically. If multiple cars have the same make,
    sort them by model alphabetically. If those cars also have the same model, then the order
    of those cars doesn't matter.

    :param cars: The list of cars to search through.
    :param feature: The given feature.
    :return: The list of cars that have the specified feature.
    """
    cars_with_feature = []
    for car in cars:
        if feature in car.features:
            cars_with_feature.append(car)

    return sort_cars_by_make(cars_with_feature)


def fuel_needed(car: Car, distance: int) -> float:
    """
    Calculate the amount of fuel needed for a given distance based on the car's fuel consumption.

    :param car: The car object representing the vehicle.
    :param distance: The distance in kilometers for which the fuel amount is calculated.
    :return: The amount of fuel needed in liters.
    """
    return (car.fuel_consumption * distance) / 100


def calculate_average_fuel_consumption(cars: list[Car]) -> float:
    """
    Calculate the average fuel consumption of the given cars.

    The average fuel consumption is the sum of the fuel consumption of all the cars divided by the number of cars.

    :param cars: The list of cars to calculate the average fuel consumption for.
    :return: The average fuel consumption of the given cars.
    """
    total_consumption = 0
    for car in cars:
        total_consumption += car.fuel_consumption

    return total_consumption / len(cars)


def most_popular_feature(cars: list[Car]) -> str:
    """
    Find the most popular feature among the given cars.

    The most popular feature is the feature that occurs the most times among all the cars.
    If multiple features occur the same number of times, return any of them.

    :param cars: The list of cars to search through.
    :return: The most popular feature among the given cars.
    """
    feature_list = []
    for car in cars:
        feature_list += car.features

    count_dict = {}
    for feature in feature_list:
        if feature in count_dict:
            count_dict[feature] += 1
        else:
            count_dict[feature] = 1

    return max(count_dict, key=count_dict.get)



def write_cars_to_file(cars: list[Car], file_name: str):
    """
    Write the given list of cars to the given file in JSON format.

    The cars should be written as a list of dictionaries, where each dictionary represents a car.
    The keys of the dictionaries should be the attributes of the car and the values should be
    the values of the attributes. The order of the cars in the list should stay the same.

    :param cars: The list of cars to write to the file.
    :param file_name: The name of the file to write the cars to.
    """
    car_list = []
    for car in cars:
        car_dict = {
            "make": car.make,
            "model": car.model,
            "fuel_consumption": car.fuel_consumption,
            "features": car.features
        }
        car_list.append(car_dict)

    with open(file_name, "w") as file:
        json.dump(car_list, file, indent=2)

def read_cars_from_file(file_name: str) -> list[Car]:
    """
    Read a list of cars from the given file in JSON format.

    The file should contain a list of dictionaries where each dictionary represents a car.
    The keys of the dictionaries should be the attributes of the car and the values should be
    the values of the attributes. The order of the cars in the list should stay the same.

    :param file_name: The name of the file to read the cars from.
    :return: The list of cars read from the file.
    """
    cars = []
    with open(file_name, 'r') as file:
        car_list = json.load(file)

        for car_data in car_list:
            car = Car(car_data['make'], car_data['model'], car_data['fuel_consumption'], car_data['features'])
            cars.append(car)

    return cars


if __name__ == '__main__':
    list_of_cars = [Car('BMW', 'X5', 12.3, ['leather', 'heated seats', 'GPS']),
                    Car('BMW', 'X6', 7.2, ['leather', 'heated seats', 'panorama', 'GPS']),
                    Car('Audi', 'A6', 9.93, ['leather', 'heated seats', 'panorama', 'GPS']),
                    Car('Audi', 'A7', 15.21, ['leather', 'heated seats', 'panorama', 'sport package']),
                    Car('Mercedes', 'S500', 10.6, ['leather', 'panorama', 'sport package',
                                                   'premium sound system'])]

    print(list_of_cars)  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]
    print(sort_cars_by_make(list_of_cars))  # [Audi A6, Audi A7, BMW X5, BMW X6, Mercedes S500]
    print()

    print(find_cars_by_make_and_model(list_of_cars, 'BMW', 'X6'))  # [BMW X6]
    print(find_cars_by_feature(list_of_cars, 'panorama'))  # [Audi A6, Audi A7, BMW X6, Mercedes S500]
    print()

    print(fuel_needed(list_of_cars[0], 150))  # 18.45; might be a little different due to floating point arithmetic errors
    print(calculate_average_fuel_consumption(list_of_cars))  # 11.048
    print()

    print(most_popular_feature(list_of_cars))  # leather
    write_cars_to_file(list_of_cars, 'cars.json')
    print(read_cars_from_file('cars.json'))  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]