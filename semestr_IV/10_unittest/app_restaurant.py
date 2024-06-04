class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' пропонує кухню типу '{self.cuisine_type}'.")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' відкритий!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["ваніль", "шоколад", "полуниця"]

    def display_flavors(self):
        print(f"Сорти морозива у кіоску '{self.restaurant_name}': {', '.join(self.flavors)}")

if __name__=="__main__":
    restaurant = Restaurant("Липа", "українська")
    print(f"Назва ресторану: {restaurant.restaurant_name}")
    print(f"Тип кухні: {restaurant.cuisine_type}")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant1 = Restaurant("Челентано", "італійська")
    restaurant2 = Restaurant("Мацурі", "японська")
    restaurant3 = Restaurant("Франче", "французька")
    print(f"Кількість обслужених відвідувачів: {restaurant.number_served}")
    restaurant.number_served = 10
    print(f"Оновлена кількість обслужених відвідувачів: {restaurant.number_served}")
    restaurant.set_number_served(20)
    print(f"Оновлена кількість обслужених відвідувачів: {restaurant.number_served}")
    restaurant.increment_number_served(5)
    print(f"Оновлена кількість обслужених відвідувачів: {restaurant.number_served}")
    ice_cream_stand = IceCreamStand("Кавова кімната", "морозиво")
    ice_cream_stand.display_flavors()