from pymol import cmd

cmd.load("cgo_arrow.py")
cmd.set("sphere_transparency", ".3")
cmd.set("sphere_scale", ".3")
cmd.set("two_sided_lighting", "on")
cmd.set("reflect", 0)
cmd.set("ambient", 0.5)
cmd.set("ray_trace_mode",  0)
cmd.set('''ray_opaque_background''', '''off''')
#
cmd.load("../../structures/exposed/4cmh/4cmh_complex_BC_A.pdb")
cmd.hide("cartoon")
cmd.show("lines", "resi 79 and chain A or resi 92 and chain C")
cmd.zoom("resi 79 and chain A or resi 92 and chain H")
cmd.origin("resi 79 and chain A or resi 92 and chain H")
#cmd.show("spheres", "id 261+4340+4344+258+4341+4342+4343")
cmd.color("brown", "id 261+4340+4344+258+4341+4342+4343")
cmd.show("spheres", "id 261 or id 263 or id 4342")
cmd.color("yellow", "id 262 or id 264")
#cmd.show("spheres", "id 263")
cmd.label("id 261", "name") 
#cmd.label("id 262", "name") 
cmd.label("id 263", "name") 
cmd.label("id 4342", "name") 
cmd.set("label_position", "(0, 0, 4)")
cmd.set("label_size", "40")
cmd.set("label_color", "black")
#
cgo_arrow("id 4342", "id 263", radius = .08, gap = .1, hradius = .25, color = "blue", name = "arrow_CE1_ND1")
#cgo_arrow("id 4342", "id 262", radius = .08, gap = .1, hradius = .25, color = "gray", name = "arrow_CE1_CG")
cgo_arrow("id 4342", "id 261", radius = .08, gap = .1, hradius = .25, color = "gray", name = "arrow_CE1_CB")
#cgo_arrow("id 262", "id 263", radius = .08, gap = .1, hradius = .25, color = "blue", name = "arrow_CG_ND1")
cgo_arrow("id 261", "id 263", radius = .08, gap = .1, hradius = .25, color = "blue", name = "arrow_CB_ND1")
#
cmd.set_view (\
    '''-0.409957051,    0.869151294,   -0.276588470,\
    -0.216349974,   -0.387256026,   -0.896226645,\
    -0.886068046,   -0.307574332,    0.346799523,\
    -0.000225172,   -0.000164923,  -20.775115967,\
     8.694190979,   -1.272594452,  -26.181915283,\
  -182.291748047,  243.358016968,  -20.000000000''')
cmd.origin("id 263")
#
cmd.png("cSI_hydro.png", width=500, height=400, dpi=600, ray=1)
