from data import *

# class planet:
#     def __init__(self, name, xp, yp, zp, xv, yv, zv):
#         self.name = name
#         self.xp, self.yp, self.zp = xp, yp, zp
#         self.xv, self.yv, self.zv = xv, yv, zv
#         self.xlist, self.ylist, self.zlist = [],[],[]

#     def __str__(self):
#          return f"Planet {self.name}:\n - Position: {self.xp, self.yp, self.zp}\n - Velocity: {self.xv, self.yv, self.zv}"

# venus = planet("venus", 0.72*AU, 0, 0, 0, v_ap_v, 0)
# print(venus)

# earth = planet("earth", 1.0167*AU, 0, 0, 0, e_ap_v, 0)
# print(earth)

# mars = planet("mars", 1.666*AU, 0, 0, 0, m_ap_v, 0)
# print(mars)

# comet = planet("comet", 1.0167*AU, 0, 0, 0, e_ap_v*0.9, 0)
# print(comet)

# sun = planet("sun", 0, 0, 0, 0, 0, 0)
# print(sun)

# setup the starting conditions
# venus
xv,yv,zv    = 0.72*AU,0,0
xvv,yvv,zvv  = 0,v_ap_v,0

# earth
xe,ye,ze    = 1.0167*AU,0,0
xve,yve,zve = 0,e_ap_v,0

# mars
xm,ym,zm    = 1.666*AU,0,0
xvm,yvm,zvm = 0,m_ap_v,0

# comet
xc,yc,zc    = 1.0167*AU,0,0
xvc,yvc,zvc = 0,e_ap_v*0.9,0

# sun
xs,ys,zs    = 0,0,0
xvs,yvs,zvs = 0,0,0

t           = 0.0
dt          = 1*daysec # every frame move this time

xvlist,yvlist,zvlist = [],[],[]
xelist,yelist,zelist = [],[],[]
xslist,yslist,zslist = [],[],[]
xmlist,ymlist,zmlist = [],[],[]
xclist,yclist,zclist = [],[],[]


def compute(xe, ye, ze, xve, yve, zve):
    # compute G force
    #rx,ry,rz = xs - xe, ys - ye, zs - ze
    rx,ry,rz = xe - xs, ye - ys, ze - zs
    modr3_e = (rx**2+ry**2+rz**2)**1.5
    fx_e = -gravconst_e*rx/modr3_e
    fy_e = -gravconst_e*ry/modr3_e
    fz_e = -gravconst_e*rz/modr3_e
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xve += fx_e*dt/Me
    yve += fy_e*dt/Me
    zve += fz_e*dt/Me
    
    # update position
    xe += xve*dt
    ye += yve*dt 
    ze += zve*dt
    
    # save the position in list
    return xe, ye, ze, fx_e, fy_e, fz_e, xve, yve, zve

# start simulation
while t<5*365*daysec:
    # ################ venus #############
    xv, yv, zv, fx_v, fy_v, fz_v, xvv, yvv, zvv = compute(xv, yv, zv, xvv, yvv, zvv)
    xvlist.append(xv)
    yvlist.append(yv)
    zvlist.append(zv)

    # ################ earth #############
    xe, ye, ze, fx_e, fy_e, fz_e, xve, yve, zve = compute(xe, ye, ze, xve, yve, zve)
    xelist.append(xe)
    yelist.append(ye)
    zelist.append(ze)
    
    # ################ Mars ##############
    xm, ym, zm, fx_m, fy_m, fz_m, xvm, yvm, zvm = compute(xm, ym, zm, xvm, yvm, zvm)
    xmlist.append(xm)
    ymlist.append(ym)
    zmlist.append(zm)
    
    # ################ comet ##############
    xc, yc, zc, fx_c, fy_c, fz_c, xvc, yvc, zvc = compute(xc, yc, zc, xvc, yvc, zvc)
    xclist.append(xc)
    yclist.append(yc)
    zclist.append(zc)
    
    ################ the sun ###########
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvs += -(fx_e+fx_m)*dt/Ms
    yvs += -(fy_e+fy_m)*dt/Ms
    zvs += -(fz_e+fz_m)*dt/Ms
    
    # update position
    xs += xvs*dt
    ys += yvs*dt 
    zs += zvs*dt
    xslist.append(xs)
    yslist.append(ys)
    zslist.append(zs)
    
    # update dt
    t +=dt

print('data ready')
#print(xalist,yalist)

#%% plot it 
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
matplotlib.rcParams['animation.embed_limit'] = 2**128
#matplotlib.use("TkAgg") # for mac M1
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(10,10))
ax.set_aspect('equal')
ax.grid()

line_v,     = ax.plot([],[],'-g',lw=1)
point_v,    = ax.plot([AU*0.72], [0], marker="o", markersize=4, markeredgecolor="orange", markerfacecolor="orange")
text_v      = ax.text(AU*0.72,0,'Venus')

line_e,     = ax.plot([],[],'-g',lw=1)
point_e,    = ax.plot([AU], [0], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
text_e      = ax.text(AU,0,'Earth')

line_m,     = ax.plot([],[],'-g',lw=1)
point_m,    = ax.plot([1.666*AU], [0], marker="o", markersize=3, markeredgecolor="red", markerfacecolor="red")
text_m      = ax.text(1.666*AU,0,'Mars')

line_c,     = ax.plot([],[],'-g',lw=1)
point_c,    = ax.plot([2*AU], [0], marker="o", markersize=2, markeredgecolor="black", markerfacecolor="black")
text_c      = ax.text(2*AU,0,'Comet')

point_s,    = ax.plot([0], [0], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
text_s      = ax.text(0,0,'Sun')

vxdata,vydata = [],[]                   # venus track
exdata,eydata = [],[]                   # earth track
sxdata,sydata = [],[]                   # sun track
mxdata,mydata = [],[]                   # mars track
cxdata,cydata = [],[]                   # comet track

print(len(xelist))

def update(i):
    vxdata.append(xvlist[i])
    vydata.append(yvlist[i])

    exdata.append(xelist[i])
    eydata.append(yelist[i])
    
    mxdata.append(xmlist[i])
    mydata.append(ymlist[i])
    
    cxdata.append(xclist[i])
    cydata.append(yclist[i])

    line_v.set_data(vxdata,vydata)
    point_v.set_data(xvlist[i],yvlist[i])
    text_v.set_position((xvlist[i],yvlist[i]))

    line_e.set_data(exdata,eydata)
    point_e.set_data(xelist[i],yelist[i])
    text_e.set_position((xelist[i],yelist[i]))
    
    line_m.set_data(mxdata,mydata)
    point_m.set_data(xmlist[i],ymlist[i])
    text_m.set_position((xmlist[i],ymlist[i]))
    
    line_c.set_data(cxdata,cydata)
    point_c.set_data(xclist[i],yclist[i])
    text_c.set_position((xclist[i],yclist[i]))
    
    point_s.set_data(xslist[i],yslist[i])
    text_s.set_position((xslist[i],yslist[i]))
    
    ax.axis('equal')
    ax.set_xlim(-3*AU,3*AU)
    ax.set_ylim(-3*AU,3*AU)
    #print(i)
    return line_v,point_v,text_v,line_e,point_s,point_e,line_m,point_m,text_e,text_m,text_s,line_c,point_c,text_c

anim = animation.FuncAnimation(fig,func=update,frames=len(xelist),interval=1,blit=True)
plt.show()

#%% to show in Jupyter Notebook 
# from IPython.display import HTML
# HTML(anim.to_jshtml())
