git init
git add .  # Add all files in the current directory
git commit -m "Initial commit"
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math as m
from mpl_toolkits.mplot3d import Axes3D
git remote add origin 


def draw_plate(ax):
    # Define the side length and height
    side_length = 64
    height = 69.8

    # Calculate the half side length
    half_side = side_length / 2

    # Define the corner points of the square (centered at (0, 0))
    corner_points = np.array([
        [-half_side, -half_side, 69.8],
        [half_side, -half_side, 69.8],
        [half_side, half_side, 69.8],
        [-half_side, half_side, 69.8]
    ])


    # Plot the square
    for i in range(4):
        ax.plot([corner_points[i, 0], corner_points[(i + 1) % 4, 0]],
                [corner_points[i, 1], corner_points[(i + 1) % 4, 1]],
                [corner_points[i, 2], corner_points[(i + 1) % 4, 2]], color='b')

    # Set the z-coordinate for the top face (parallel to xy-plane)
    z_top = height
    top_square = np.array([
        [point[0], point[1], z_top] for point in corner_points
    ])

    # Plot the top face
    for i in range(4):
        ax.plot([top_square[i, 0], top_square[(i + 1) % 4, 0]],
                [top_square[i, 1], top_square[(i + 1) % 4, 1]],
                [top_square[i, 2], top_square[(i + 1) % 4, 2]], color='b')
        
def fun2(t,p,h):
    x=[]
    y=[]
    z=[]
    for i in range (len(t)):
        rho=h/(np.cos(t[i]))
        x.append(rho*np.sin(t[i])*np.cos(p[i]))
        y.append(rho*np.sin(t[i])*np.sin(p[i]))
        z.append(h)
    return x,y,z

def plot_angles(t,p,h,ax,x_offset=0,y_offset=0,plot_color=None,plot_marker=None,plot_label=None):#theta, phi, height, ax
    t = [x*m.pi/180 for x in t]
    p = [x*m.pi/180 for x in p]
    x=fun2(t,p,h)[0]
    y=fun2(t,p,h)[1]
    z=fun2(t,p,h)[2]

    x=[_ + x_offset for _ in x]
    y=[_ + y_offset for _ in y]
    
    print(zip(x,y,z))
    ax.scatter(x,y,z,color=plot_color,marker=plot_marker,label=plot_label)
    
    for i in range(len(x)):
        ax.text(x[i], y[i], z[i], f"{i+1}", size=10, color="black")


#P1 plots=======================================================================
fig=plt.figure()
ax=plt.axes(projection='3d')

h=69.8

#Ground truth
x0=[-25.3,0.01,24.6,-25.4,0.01,24.7,-25.1,0.01,25.2]
y0=[-25.3,-25.3,-25.1,0,-0.02,0,24.6,24.5,24.5]
z0=[69.8]*9

#ground truth plot
ax.scatter(x0,y0,z0,color='red',marker='x',label='Ground Truth')
for i in range(len(x0)):
    ax.text(x0[i], y0[i], z0[i], f"x{i+1}", size=10, color="black")
    
#trial 1
t1=[14.55,17.27,21.82,16.36,2.73,25.45,20.91,14.54,22.73]
p1=[236.3,272.7,309,181.8,236.4,0,127.27,94.55,47.27]

plot_angles(t1,p1,h,ax,plot_color='green',plot_label='Trial 1')
#trial 2
t2=[13.64,16.36,24.55,20,4.55,17.27,25.45,18.18,33.64]
p2=[225.45,280,309.1,189,138.18,21.8,123.64,87.27,43.64]

plot_angles(t2,p2,h,ax,plot_color='blue',plot_marker='^',plot_label='Trial 2')
#trial 3
t3=[13.64,17.25,42.73,18.18,2.73,14.55,25.45,10.91,15.45]
p3=[236.36,294.55,323.64,200,352.73,345.45,134.55,101.82,40]

plot_angles(t3,p3,h,ax,plot_color='orange',plot_marker='*',plot_label='Trial 3')

plt.legend()

draw_plate(ax)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-35, 35])
ax.set_ylim([-35, 35])
ax.set_zlim([60, 82])

#P3 plots======================================================================
fig=plt.figure()
ax=plt.axes(projection='3d')

h=69.8
x_offs=79
y_offs=52
#Ground truth
x0=[-25.3,0.01,24.6,-25.4,0.01,24.7,-25.1,0.01,25.2]
y0=[-25.3,-25.3,-25.1,0,-0.02,0,24.6,24.5,24.5]
z0=[69.8]*9

#ground truth plot
ax.scatter(x0,y0,z0,color='red',marker='x',label='Ground Truth')
for i in range(len(x0)):
    ax.text(x0[i], y0[i], z0[i], f"x{i+1}", size=10, color="black")
    
#trial 1
t1=[63.64,53.64,56.36,55.45,50.91,49.09,40.91,50.91,39.09]
p1=[203.64,221.82,225.45,196.36,203.64,200,192.73,196.36,178.18]

plot_angles(t1,p1,h,ax,x_offset=x_offs,y_offset=y_offs,plot_color='green',plot_label='Trial 1')

#trial 3
t3=[70,55.45,55.45,50,56.36,56.36,45.45,38.18,49.09]
p3=[185.45,214.55,218.18,200,192.73,181.82,192.73,178.18,189.09]

plot_angles(t3,p3,h,ax,x_offset=x_offs,y_offset=y_offs,plot_color='orange',plot_marker='*',plot_label='Trial 3')


#trial 2
t2=[76.36,52.73,61.82,56.36,52.73,48.18,49.09,46.36,50.91]
p2=[203.64,200,232.73,189.09,210.91,200,181.82,192.73,189.09]

plot_angles(t2,p2,h,ax,x_offset=x_offs,y_offset=y_offs,plot_color='blue',plot_marker='^',plot_label='Trial 2')

plt.legend()
draw_plate(ax)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-35, 35])
ax.set_ylim([-35, 35])
ax.set_zlim([60, 82])

# Show the plot
plt.show()
