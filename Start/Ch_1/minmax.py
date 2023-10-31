# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
# print(f"Min values: {min(values)}")
# print(f"Min values: {min(strings)}")

# # TODO: The max() function finds the maximum value
# print(f"Max values: {max(values)}")
# print(f"Max values: {max(strings)}")

# # TODO: define a custom "key" function to extract a data field
# print(f"Min values: {min(strings, key=len)}")
# print(f"Max values: {max(strings, key=len)}")

# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(type(data))