import bpy
import random

# Constancies
NUMBER_OF_SHEETS = 100
GAP = 0.1
MAX_HEIGHT = 10.2
MIN_HEIGHT = 9.8
MAX_THICKNESS = 0.2
MIN_THICKNESS = 0.3
MAX_ANGLE = -0.1
MIN_ANGLE = 0.1

def clean_scene():
  for obj in bpy.data.objects:
    bpy.data.objects.remove(obj)

  for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(mesh)

def create_plank(height, thickness, angle):
  bpy.ops.mesh.primitive_cube_add(
    size=1, 
    location=(0, 0, 0),
    rotation=(0, 0, angle)
  )
  bpy.ops.transform.resize(value=(thickness, 1, height), orient_type='LOCAL')
  bpy.ops.transform.translate(value=(0, 0, height*0.5), orient_type='LOCAL')

def main():
    GAT = 0.1
    for i in range(NUMBER_OF_SHEETS):
      height = random.uniform(MIN_HEIGHT, MAX_HEIGHT)
      thickness  = random.uniform(MIN_THICKNESS, MAX_THICKNESS)
      angle  = random.uniform(MIN_ANGLE, MAX_ANGLE)

      create_plank(height, thickness, angle)
      bpy.ops.transform.translate(value=(0, (1+GAP)*i, 0))
  
clean_scene()
main()
