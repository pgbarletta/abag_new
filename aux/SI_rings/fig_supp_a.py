from pymol.cmd import *

set("sphere_transparency", ".3")
set("sphere_scale", ".75")
set("two_sided_lighting", "on")
set("reflect", 0)
set("ambient", 0.5)
set("ray_trace_mode",  0)
set('''ray_opaque_background''', '''off''')
#
load("../../structures/exposed/7nd7/7nd7_complex_HL_A.pdb")
hide("cartoon")
show("lines", "resi 93 and chain L")
show("lines", "resi 486 and chain A")
#cmd.zoom("resi 200 and chain A or resi 50 and chain L")
#cmd.orient("resi 200 and chain A or resi 50 and chain L")
show("spheres", "resi 93  and chain L")
show("spheres", "resi 486 and chain A")
#label("id 3201",  "resi") 
#label("id 25092", "resi") 
#label("id 3201",  "resn") 
#label("id 25092", "resn") 
#set("label_position", "(0, 0, 4)")
#set("label_size", "40")
#set("label_color", "blue")
origin("resi 93 and chain L")
#cmd.distance("id 4180", "id 1585")
#
set_view (\
    '''-0.156866536,   -0.697831750,   -0.698872328,\
     0.984359384,   -0.167916059,   -0.053281683,\
    -0.080170304,   -0.696300447,    0.713258922,\
    -0.000167899,    0.000121519,  -55.559085846,\
   203.854125977,  222.878250122,  172.077774048,\
   -69.311889648,  180.417556763,  -20.000000000''')
#
cmd.png("aSI_ring.png", width=500, height=400, dpi=600, ray=1)
