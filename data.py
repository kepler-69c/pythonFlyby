"""physical constants used in all programs"""

G           = 6.67e-11
Ms          = 2.0e30             # sun
Mc          = 0.33010e24         # mercury
Mv          = 4.8673e24          # venus
Me          = 5.9722e24          # earth        
Mm          = 6.39e23            # mars
daysec      = 24.0*60*60

gravconst_e = G*Me*Ms
gravconst_m = G*Mm*Ms
gravconst_c = G*Mc*Ms
