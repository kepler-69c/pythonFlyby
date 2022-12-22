from celestialBodies import planet, spaceProbe
from data import *

start = "2021-11-21"

sun = planet("Sun", 10, start=start)
venus = planet("Venus", 299, start=start)
earth = planet("Earth", 399, start=start)
mars = planet("Mars", 499, start=start)

probe = spaceProbe(Me, sun, venus, earth, mars, "1d")

# space probe ############################################################
# earth
xe,ye,ze    = earth.x[0],earth.y[0],earth.z[0]
xve,yve,zve = earth.vx[0]/daysec,earth.vy[0]/daysec,earth.vz[0]/daysec
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
# animation ###########################################################################################################
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
matplotlib.rcParams['animation.embed_limit'] = 2**128
matplotlib.use("TkAgg") # for mac
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(10,10))
ax.set_aspect('equal')
ax.grid()

line_a,     = ax.plot([],[],'-g',lw=1)
point_a,    = ax.plot([AU], [0], marker="o", markersize=4, markeredgecolor="brown", markerfacecolor="brown")
text_a      = ax.text(AU,0,'Venus')

line_b,     = ax.plot([],[],'-g',lw=1)
point_b,    = ax.plot([1.5*AU], [0], marker="o", markersize=3, markeredgecolor="blue", markerfacecolor="blue")
text_b      = ax.text(1.666*AU,0,'Earth')

line_c,     = ax.plot([],[],'-g',lw=1)
point_c,    = ax.plot([2*AU], [0], marker="o", markersize=2, markeredgecolor="red", markerfacecolor="red")
text_c      = ax.text(2*AU,0,'Mars')

line_d,     = ax.plot([],[],'-g',lw=1)
point_d,    = ax.plot([2*AU], [0], marker="o", markersize=2, markeredgecolor="black", markerfacecolor="black")
text_d      = ax.text(2*AU,0,'Space Probe')

point_e     = ax.plot([0], [0], marker="o", markersize=8, markeredgecolor="yellow", markerfacecolor="yellow")
text_e      = ax.text(0,0,"Sun")

text_date   = ax.text(-2.5*1E11, 2.4*1E11, earth.start)

axdata,aydata = [],[] # venus track
bxdata,bydata = [],[] # earth track
cxdata,cydata = [],[] # mars track
dxdata,dydata = [],[] # space probe track

def update(i):
    axdata.append(venus.x[i])
    aydata.append(venus.y[i])
    
    bxdata.append(earth.x[i])
    bydata.append(earth.y[i])
    
    cxdata.append(mars.x[i])
    cydata.append(mars.y[i])

    dxdata.append(xelist[i])
    dydata.append(yelist[i])
    
    line_a.set_data(axdata,aydata)
    point_a.set_data(venus.x[i],venus.y[i])
    text_a.set_position((venus.x[i],venus.y[i]))
    
    line_b.set_data(bxdata,bydata)
    point_b.set_data(earth.x[i],earth.y[i])
    text_b.set_position((earth.x[i],earth.y[i]))
    
    line_c.set_data(cxdata,cydata)
    point_c.set_data(mars.x[i],mars.y[i])
    text_c.set_position((mars.x[i],mars.y[i]))

    line_d.set_data(dxdata,dydata)
    point_d.set_data(xelist[i],yelist[i])
    text_d.set_position((xelist[i],yelist[i]))

    ax.axis('equal')
    ax.set_xlim(-2*AU,2*AU)
    ax.set_ylim(-2*AU,2*AU)

    text_date.set_text(earth.d[i])

    return line_a,point_a,text_a,line_b,point_b,text_b,line_c,point_c,text_c,line_d,point_d,text_d,text_date

anim = animation.FuncAnimation(fig,func=update,frames=len(earth.x),interval=10,blit=True)
plt.show()
