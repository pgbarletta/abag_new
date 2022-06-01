from pymol.cmd import *

set("sphere_transparency", ".3")
set("sphere_scale", ".75")
set("two_sided_lighting", "on")
set("reflect", 0)
set("ambient", 0.5)
set("ray_trace_mode",  0)
set('''ray_opaque_background''', '''off''')
#
load("reduced_1afv.pdb")
hide("cartoon")
hide("nonbonded")
show("cartoon", "chain A or chain H")
color("orange", "chain A")
color("blue", "chain H")
show("lines", "resi 76 and chain A")
show("lines", "resi 103 and chain H")
show("spheres", "resi 76 and chain A")
show("spheres", "resi 103 and chain H")

spectrum("elem", "rainbow", "resi 76 and chain A")
spectrum("elem", "rainbow", "resi  103 and chain H")

color("atomic", "resi 76 and chain A")
color("atomic", "resi 103 and chain H")
origin("resi 76 and chain A")

distance("da1", "id 4814", "id 582", 4, 2)
hide("labels")
#
set_view (\
    '''-0.333511770,    0.518017232,   -0.787670195,\
     0.056317985,    0.844962239,    0.531850517,\
     0.941060781,    0.133017465,   -0.310979962,\
    -0.000204559,   -0.000255173,  -35.810398102,\
    30.739141464,   20.340734482,   92.212593079,\
   -58.367538452,  129.979843140,  -20.000000000''')
#
cmd.png("aSI_polar.png", width=500, height=400, dpi=600, ray=1)
