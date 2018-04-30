# Create a variable named `cars` to store the number of cars available today
# Store value 100 in this variable - 100 cars today
cars = 100

# Create a varialbe space_in_a_car to store the number of passengers each car can transport
# Store value 4.0 in this variable - each car can transport 4 people
space_in_a_car = 4.0

# Create a variable to store the number of drivers available today
# Store 30 in this variable - 30 drivers available
drivers = 30

# Create a variable to stroe the number of passengers that have to be transported
# Store 90 in this variable - 90 passengers for carpool
passengers = 90

# Since more cars than drivers, some cars will not have anyone to drive them. 
# Calculate how many cars won't have drivers, store result in variable cars_not_driven
cars_not_driven = cars - drivers

# Naturally, the total number of cars driven = total number of drivers. Straightforward assignment
# by fetching value stored in drivers and assigning it the cars_driven variable as well
cars_driven = drivers

# Calculate total number of people that can be transported, including drivers
# 4 people per car * 30 cars today
carpool_capacity = cars_driven * space_in_a_car

# Find how many people need to be placed in each car on average
average_passengers_per_car = passengers / cars_driven


# Print carpool summary by accessing values stored in the variables
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about ", average_passengers_per_car, "in each car.")