"""physical constants used in all programs"""

G           = 6.67e-11
Mb          = 4.0e30                    # black hole
Ms          = 2.0e30                    # sun
Me          = 5.972e24                  # earth        
Mm          = 6.39e23                   # mars
Mc          = 6.39e20                   # unknown comet
AU          = 1.5e11
daysec      = 24.0*60*60

e_ap_v      = 29290                     # earth velocity at aphelion
m_ap_v      = 21970                     # mars velocity at aphelion
commet_v    = 7000

gravconst_e = G*Me*Ms
gravconst_m = G*Mm*Ms
gravconst_c = G*Mc*Ms