"""physical constants used in all programs"""

G           = 6.67e-11
Mb          = 4.0e30             # black hole
Ms          = 2.0e30             # sun
Mc          = 0.33010e24         # mercury
Mv          = 4.8673e24          # venus
Me          = 5.9722e24          # earth        
Mm          = 6.39e23            # mars
Mc          = 6.39e20            # unknown comet
AU          = 1.5e11
daysec      = 24.0*60*60

c_ap_v      = 38860              # aphelion velocity mercury	
v_ap_v      = 34790              # aphelion velocity mercury
e_ap_v      = 29290              # earth velocity at aphelion
m_ap_v      = 21970              # mars velocity at aphelion
commet_v    = 7000

gravconst_e = G*Me*Ms
gravconst_m = G*Mm*Ms
gravconst_c = G*Mc*Ms
