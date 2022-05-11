import bpy

bpy.ops.mesh.primitive_cube_add()
obj = bpy.context.active_object

new_mat = bpy.data.materials.new(name = "My Material")
obj.data.materials.append(new_mat)

new_mat.use_nodes = True
nodes = new_mat.node_tree.nodes

material_output = nodes.get("Material Output")

node_emission = nodes.new(type='ShaderNodeEmission')
node_emission.inputs[0].default_value = ( 0.0, 0.3, 1.0, 1 ) #Color
node_emission.inputs[1].default_value = 500.0 #strength

links = new_mat.node_tree.links
new_link = links.new(node_emission.outputs[0], material_output.inputs[0])
