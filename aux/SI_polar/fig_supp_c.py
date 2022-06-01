from pymol.cmd import *

set("sphere_transparency", ".3")
set("sphere_scale", ".75")
set("two_sided_lighting", "on")
set("reflect", 0)
set("ambient", 0.5)
set("ray_trace_mode",  0)
set('''ray_opaque_background''', '''off''')
#
load("reduced_1bj1.pdb")
hide("cartoon")
hide("nonbonded")
show("cartoon", "chain W or chain L")
color("orange", "chain W")
color("blue", "chain L")
show("nonbonded", "id 8549 or id 8184")
show("spheres", "id 8549 or id 8184")
color("red", "id 8549 or id 8184")
show("lines", "resi 91 and chain L")
show("lines", "resi 94 and chain L")
show("lines", "resi 87 and chain W")
show("spheres", "resi 91 and chain L")
show("spheres", "resi 94 and chain L")
show("spheres", "resi 87 and chain W")

spectrum("elem", "rainbow", "resi 91 and chain L")
spectrum("elem", "rainbow", "resi 94 and chain L")
spectrum("elem", "rainbow", "resi 87 and chain W")

color("atomic", "resi 91 and chain L")
color("atomic", "resi 94 and chain L")
color("atomic", "resi 87 and chain W")
origin("id 8549")

distance("da1", "id 8184", "resi 87 and chain W", 4, 2)
distance("da2", "id 8184", "resi 91 and chain L", 4, 2)

distance("db1", "id 8549", "resi 87 and chain W", 4, 2)
distance("db2", "id 8549", "resi 94 and chain L", 4, 2)
hide("labels")
#
set_view (\
    '''-0.679921031,    0.692060232,   -0.242395401,\
     0.470925152,    0.665484250,    0.579096794,\
     0.562073708,    0.279590070,   -0.778386652,\
    -0.000246947,   -0.000217207,  -47.730491638,\
    12.038813591,    6.136070251,   18.787843704,\
  -523.673461914,  619.162597656,  -20.000000000''')
#
#cmd.png("cSI_polar.png", width=500, height=400, dpi=600, ray=1)
