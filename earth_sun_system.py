from math import sqrt
from data import *
import matplotlib.pyplot as plt

# earth
xe,ye,ze    = 1.0167*AU,0,0
xve,yve,zve = 0,e_ap_v,0
# sun
xs,ys,zs    = 0,0,0
xvs,yvs,zvs = 0,0,0

t           = 0.0
dt          = 1*daysec # every frame move this time

xelist,yelist,zelist = [],[],[]
xslist,yslist,zslist = [],[],[]

while t<5*365*daysec:
    # ################ earth #############
    rx,ry,rz = xe - xs, ye - ys, ze - zs
    modr3_e = (rx**2+ry**2)**1.5#+rz**2)**1.5
    fx_e = -gravconst_e*rx/modr3_e
    fy_e = -gravconst_e*ry/modr3_e
    # fz_e = -gravconst_e*rz/modr3_e
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xve += fx_e*dt/Me
    yve += fy_e*dt/Me
    # zve += fz_e*dt/Me
    
    # update position
    xe += xve*dt
    ye += yve*dt 
    # ze += zve*dt

    xelist.append(xe)
    yelist.append(ye)
    # zelist.append(ze)
    
    # update dt
    t +=dt

plt.scatter(xelist, yelist)
plt.show()