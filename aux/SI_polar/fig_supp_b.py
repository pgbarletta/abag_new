from pymol.cmd import *

set("sphere_transparency", ".3")
set("sphere_scale", ".75")
set("two_sided_lighting", "on")
set("reflect", 0)
set("ambient", 0.5)
set("ray_trace_mode",  0)
set('''ray_opaque_background''', '''off''')
#
load("reduced_1adq.pdb")
hide("cartoon")
hide("nonbonded")
show("cartoon", "chain A or chain H")
color("orange", "chain A")
color("blue", "chain H")
show("lines", "resi 255 and chain A")
show("lines", "resi 31 and chain H")
show("spheres", "resi 255 and chain A")
show("spheres", "resi 31 and chain H")

spectrum("elem", "rainbow", "resi 255 and chain A")
spectrum("elem", "rainbow", "resi  31 and chain H")

color("atomic", "resi 255 and chain A")
color("atomic", "resi 31 and chain H")
origin("resi 255 and chain A")

distance("da1", "id 145", "id 3470", 4, 2)
hide("labels")
#
set_view (\
    '''0.193786159,   -0.774888873,   -0.601651549,\
     0.451287866,    0.614955306,   -0.646654606,\
     0.871073544,   -0.146209329,    0.468863934,\
    -0.000412625,    0.000010680,  -41.749835968,\
    13.724317551,    7.646373272,   21.669618607,\
  -529.660644531,  613.175354004,  -20.000000000''')
#
cmd.png("bSI_polar.png", width=500, height=400, dpi=600, ray=1)
