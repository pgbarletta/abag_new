from pymol.cmd import *

set("sphere_transparency", ".4")
set("sphere_scale", ".75")
set("two_sided_lighting", "on")
set("reflect", 0)
set("ambient", 0.5)
set("ray_trace_mode",  0)
set('''ray_opaque_background''', '''off''')
#
load("/home/pbarletta/labo/22/abag/structures/exposed/5vk2/5vk2_complex_DE_cC.pdb")
color("salmon", "chain c or chain C or chain .")
color("atomic", "(not elem C)")

select("id 8048+8022+8615+10552+8617+8017+5492+8608+8012+8011+5493+8020+5497+5495+8618+8614+5489+10551+8054+8037+8978+8035+8988+8034+8970+8994+8977+8995+8973+8989+7946+10505+8031+10508+10509+8589+8078+8579+8587+8087+8591+8084+8088+10030+7998+8030+10032+10511+8027+10513+8980+8982+8024+8079+8575")
set_name("sele", "cluster_1")
show("spheres", "cluster_1")
color("0x6368c1", "cluster_1")
# select("id 10040+10041+7713")
# set_name("sele", "cluster_2")
# show("spheres", "cluster_2")
# color("0x3b8128", "cluster_2")
# select("id 8598+5507+5505")
# set_name("sele", "cluster_3")
# show("spheres", "cluster_3")
# color("0x1854e8", "cluster_3")


ser="resi 54+104+56+34+58+53 and chain D"
asp="resi 401 and chain c"
asq="resi 402 and chain c"
glu="resi 404 and chain c"
show("sticks", ser)
show("spheres", ser)
show("sticks", asp)
show("sticks", asq)
show("sticks", glu)

origin(ser)
select(ser)
set_name("sele", "ser")
select("chain c")
distance(asp, ser, 4, 2)
distance(asq, ser, 4, 2)
distance(glu, ser, 4, 2)
set("label_size", "0")
set("sphere_transparency", ".1", ser)
#set("sphere_transparency", ".4", asp+" and "+asq+" and "+glu)
#
set_view (\
    '''0.269936740,   -0.946117938,   -0.178835049,\
     0.161837444,   -0.138505891,    0.977048397,\
    -0.949176490,   -0.292683750,    0.115730405,\
     0.000289605,   -0.000658179,  -55.063282013,\
   -59.087272644,   23.109546661,   22.004617691,\
     1.796229482,  138.423339844,  -20.000000000''')
#
cmd.png("fig_ser.png", width=500, height=400, dpi=600, ray=1)
