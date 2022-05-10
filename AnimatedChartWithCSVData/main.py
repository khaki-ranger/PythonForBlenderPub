import bpy
import csv
import re

FILEPATH = "Please enter your file path"


def clear_all():
  for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)


def read_file():
  results = []

  with open(FILEPATH, mode='r', encoding="shift-jis") as csv_file:
    reader = csv.reader(csv_file)
  
    for row in reader:
      try:
        if re.match(r'^\d{4}\/([1-9]|1[0-2])\/([1-9]|[12][0-9]|3[01])$', row[0]):
          results.append(
            {
              'date': row[0],
              'average': row[1],
              'max': row[4],
              'min': row[7]
            }
          )
      # Error handling
      except IndexError:
        print('Handled Error: list index out of range')

  return results


def create_bar(data):
  print(data)


def create_chart(data):
  for i in range(len(data)):
    create_bar(data[i])


def main():
  data = read_file()
  create_chart(data)
  

clear_all()

main()
