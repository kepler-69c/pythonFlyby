import matplotlib.pyplot as plt
from data import *
from celestialBodies import planet

venus = planet("Venus", 299)
earth = planet("Earth", 399)
mars = planet("Mars", 499)

# ###########################################################################################################
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

point_d     = ax.plot([0], [0], marker="o", markersize=8, markeredgecolor="yellow", markerfacecolor="yellow")
text_d      = ax.text(0,0,"Sun")

text_date   = ax.text(-2.5*AU, 2*AU, "Date")

axdata,aydata = [],[] # venus track
bxdata,bydata = [],[] # earth track
cxdata,cydata = [],[] # mars track

def update(i):
    axdata.append(venus.x[i])
    aydata.append(venus.y[i])
    
    bxdata.append(earth.x[i])
    bydata.append(earth.y[i])
    
    cxdata.append(mars.x[i])
    cydata.append(mars.y[i])
    
    line_a.set_data(axdata,aydata)
    point_a.set_data(venus.x[i],venus.y[i])
    text_a.set_position((venus.x[i],venus.y[i]))
    
    line_b.set_data(bxdata,bydata)
    point_b.set_data(earth.x[i],earth.y[i])
    text_b.set_position((earth.x[i],earth.y[i]))
    
    line_c.set_data(cxdata,cydata)
    point_c.set_data(mars.x[i],mars.y[i])
    text_c.set_position((mars.x[i],mars.y[i]))

    ax.axis('equal')
    ax.set_xlim(-2*AU,2*AU)
    ax.set_ylim(-2*AU,2*AU)
    #print(i)
    return line_a,point_a,text_a,line_b,point_b,text_b,line_c,point_c,text_c

anim = animation.FuncAnimation(fig,func=update,frames=len(earth.x),interval=10,blit=True)
plt.show()