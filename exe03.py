#-*-coding:utf-8-*-

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avrange_passengers_per_car = passengers / cars_driven

print("there are",cars,"cars available")
print("we need to put about", avrange_passengers_per_car,"in a car")

