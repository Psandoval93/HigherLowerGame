# Creating Class
class Car:

    # Defining instance method with default values
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0

    # Defining variable for car value calculation
    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    # Defined variable for printing info using class attributes
    def print_info(self):
        print("Car's information:")
        print('   Model year: {}'.format(self.model_year))
        print('   Purchase price: {}'.format(self.purchase_price))
        print('   Current value: {}'.format(self.current_value))


# Creating if statement to call class
if __name__ == "__main__":
    # Receives user input & set variables for input
    year = int(input())
    price = int(input())
    current_year = int(input())

    # Creating variables for instance methods from user input & calling defined variables
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()
