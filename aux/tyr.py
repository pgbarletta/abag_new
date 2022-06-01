from pymol.cmd import *

set("sphere_transparency", ".3")
set("sphere_scale", ".75")
set("two_sided_lighting", "on")
set("reflect", 0)
set("ambient", 0.5)
set("ray_trace_mode",  0)
set('''ray_opaque_background''', '''off''')
#
load("../structures/exposed/3cvh/3cvh_complex_HL_AC.pdb")
hide("cartoon")
tyr = "resi 101 and chain H"
lys = "resi 146 and chain A"
leu = "resi 8 and chain C"

show("sticks", tyr)
show("sticks", lys)
show("sticks", leu)
show("spheres", tyr)
show("spheres", lys)
show("spheres", leu)
distance(tyr, leu, 4, 2)

cmd.select("id 1283+1288+3083+3932+1286+5455+3934+3079+1281+5452+3929+5453+3930+3931+3935+3933+1252+3101+3082+1253+5454+1251+3098+3906+3914+1178+3921+3918+3112+1180+3911+3111+3113+3922+3908+3915+3907+3910+3110+3108+1179+3905+3909+1181+3903+1216+3894+3899+1219+3898+3896+3895+1210+3897+3893")
cmd.set_name("sele", "cluster_1")                                                             
cmd.show("spheres", "cluster_1")
cmd.color("brown", "cluster_1")

origin(tyr)
#
set_view (\
    '''0.042276297,    0.933128774,    0.357055694,\
     0.930655122,    0.093224518,   -0.353825688,\
    -0.363447875,    0.347252518,   -0.864479125,\
    -0.000039890,   -0.000118271,  -40.552757263,\
   -17.997486115,  -45.431098938,   14.557052612,\
    26.272182465,   54.838375092,  -20.000000000''')
#
cmd.png("fig_tyr.png", width=500, height=400, dpi=600, ray=1)
