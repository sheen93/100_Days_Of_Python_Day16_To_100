import pandas

primary_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

gray_squirrels = primary_data[primary_data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)
red_squirrels_count = len(primary_data[primary_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(primary_data[primary_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")