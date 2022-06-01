from pymol.cmd import *

set("sphere_transparency", ".3")
set("sphere_scale", ".75")
set("two_sided_lighting", "on")
set("reflect", 0)
set("ambient", 0.5)
set("ray_trace_mode",  0)
set('''ray_opaque_background''', '''off''')
#
load("../../structures/exposed/5i5k/5i5k_complex_XY_A.pdb")

hide("cartoon")
show("lines", "resi 99  and chain X")
show("lines", "resi 33  and chain X")
show("lines", "resi 885 and chain A")
show("spheres", "resi 99  and chain X")
show("spheres", "resi 33  and chain X")
show("spheres", "resi 885 and chain A")

origin("resi 99 and chain X")
#
set_view (\
    '''-0.994777858,   -0.085898466,   -0.055120576,\
    -0.096357949,    0.612410307,    0.784645855,\
    -0.033643473,    0.785859585,   -0.617488861,\
     0.000013652,    0.000034546,  -40.228939056,\
   -36.639923096,   52.495216370,   11.963930130,\
   -66.936874390,  147.401336670,  -20.000000000''')
#
cmd.png("bSI_ring.png", width=500, height=400, dpi=600, ray=1)
