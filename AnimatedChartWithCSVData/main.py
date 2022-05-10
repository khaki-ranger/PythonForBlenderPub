import bpy
import csv
import re

FILEPATH = "Please enter your file path"


def clear_all():
  obj.animation_data_clear()
  for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)


def clean_up():
  bpy.ops.object.select_all(action='DESELECT')


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


def add_keyframes(objects, data):
  offset = 0
  index = 0 

  for obj in objects:
    dic = data[index]
    height = float(dic['average'])
    
    obj.scale = [1, 1, 0]
    obj.keyframe_insert(data_path = "scale", frame = 1 + offset)

    obj.scale = [1, 1, height]
    obj.keyframe_insert(data_path = "scale", frame = 20 + offset)

    index += 1
    offset += 1


def create_bar_object(index):
  bpy.ops.mesh.primitive_cube_add(
    size=1, 
    enter_editmode=True, 
    align='WORLD',
    location=(0, 1 * index, 0)
  )

  bpy.ops.transform.translate(
    value=(0, 0, 0.5)
  )
  bpy.ops.object.editmode_toggle()



def create_chart(data):
  for i in range(len(data)):
    create_bar_object(i)


def main():
  data = read_file()
  create_chart(data)
  items = bpy.data.collections["Collection"].objects
  add_keyframes(objects=items, data=data)

  

clear_all()
main()
clean_up()
