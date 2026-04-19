import pandas

student_dict = {
    "student":["Angela", "Beth","Caroline", "Dave"],
    "score":[56, 85, 97, 32]
}

# for (key,value) in student_dict.items():
#     print(key, value)

student_dataframe = pandas.DataFrame(student_dict)

print(student_dataframe)

#Loop through pandas dataframe using iterrows()
for (index, row) in student_dataframe.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(f"{row.student} : {row.score}")