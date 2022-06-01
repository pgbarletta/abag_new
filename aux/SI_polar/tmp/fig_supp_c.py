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
hide("everything", "resn WAT")
show("cartoon", "chain W or chain L")
color("orange", "chain W and not resn WAT")
color("blue", "chain L and not resn WAT")

wat1="resi 1082 and chain L"
wat2="resi 1447 and chain W"
show("spheres", wat1 + " or " + wat2)
show("sticks", wat1 + " or " + wat2)

gln="resi 599 and chain W"
val="resi 91 and chain L"
tyr="resi 94 and chain L"
resis = gln + " or " + val + " or " + tyr
show("lines", resis)
show("spheres", resis)
spectrum("elem", "rainbow", resis)
color("atomic", resis)

origin(wat1)
distance("dgln1", wat1, gln, 6, 2)
distance("dtyr1", wat1, tyr, 6, 2)
distance("dtyr1", "id 16115", "id 1364", 6, 2)

distance("dgln2", wat2, gln, 6, 2)
distance("dval2", wat2, val, 6, 2)
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
