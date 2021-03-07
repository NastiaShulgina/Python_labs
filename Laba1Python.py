class Restaurant:

    __selfService = False

    @staticmethod
    def getSelfService (self):
        return Restaurant.__selfService
    
    def __init__(self, name = 'FoodEstablishment', numberDishesMenu = 50, address = 'Here is the address.', tablesQuantity = 30, 
        openingTime = '06:00', closingTime = '23:00', areaInSquareMeters = 60):
        self.name = name 
        self.numberDishesMenu = numberDishesMenu
        self.address = address
        self.tablesQuantity = tablesQuantity
        self.openingTime = openingTime
        self.closingTime = closingTime
        self.areaInSquareMeters = areaInSquareMeters
    
    def __del__(self):
        return

    def __str__(self):
        return f"\nThe name of the restaurant is {self.name}; there are {self.numberDishesMenu} " \
               f"dishes on the menu; the address is {self.address};\nthere are {self.tablesQuantity} " \
               f"tables; the restaurant opens at {self.openingTime} o'clock and closes at {self.closingTime} " \
               f"o'clock; the area of the restaurant is {self.areaInSquareMeters} square meters."


def main():
        restaurant1 = Restaurant (name = 'Avrora', numberDishesMenu = 87, address = 'Shevchenko Avenue 15', tablesQuantity = 30, 
        openingTime = '06:00', areaInSquareMeters = 100)
        restaurant2 = Restaurant ('Puzata Hata', 120, 'Doroshenka Street 62', 60, '07:00', '23:00', 150)
        restaurant3 = Restaurant (name = 'Druzi', address = 'Saksahanskoho Street 1')
        print(restaurant1.__str__())
        print(restaurant2.__str__())
        print(restaurant3.__str__())


if __name__ == "__main__":
    main()