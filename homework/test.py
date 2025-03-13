class Restaurant:
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}  {self.restaurant_type}")

    def open_restaurant(self):
        print("The restaurant is opening")

this_restaurant = Restaurant('yingying of restaurant','rice')
print (f"{this_restaurant.restaurant_name},{this_restaurant.restaurant_name}")