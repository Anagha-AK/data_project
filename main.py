import csv
top_name=""
top_marks=0

with open('data.csv','r') as file:
    reader= csv.DictReader(file)

    for row in reader:
        marks=int(row['marks'])

        if marks >top_marks:
            top_marks=marks
            top_name=row['name']
print("Top student:",top_name, top_marks)