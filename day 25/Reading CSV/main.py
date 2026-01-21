import csv

# with open("weather_data.csv", mode="r+")as weather_data:
#     data_list = weather_data.readlines()
#
# print(data_list)

# with open("weather_data.csv") as weather_data:
#     data = list(csv.reader(weather_data))
#     # data_list = list(data)
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(f"Average Temperature: {sum(temp_list)/len(temp_list)}")
print(f"Max Temperature: {data["temp"].max()}")
print(f"Average Temperature: {data.temp.mean()}")

#Get Data in row
print(f"Max temp day: \n{data[data.temp == data.temp.max()]}")

monday = data[data.day == "Monday"]
# print(monday.temp[0])
print(f"Monday temp(f): {monday.temp[0]*(9/5)+32}")

#Create data frame from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(data_dict)

print(student_data)

student_data.to_csv("student_data.csv")