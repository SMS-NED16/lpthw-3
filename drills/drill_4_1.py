cars = 100
space_in_a_car = 4		# Value is now 4 instead of 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "people in each car.")

# Using 4 instead of 4.0 for the value of space_in_a_car affects the way
# mathematical operations are performed using this variable. For example, carpool
# capacity uses space_in_a_car as an operand for multiplication. cars_driven is 
# an integer, but when space_in_a_car is a float, the result is also a float 120.0
# However, when both are integers as in this drill, the result is also an integer 120