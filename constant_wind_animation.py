import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import fire


a = 1
f = 1
g = 0.5
h = 1
t_0 = 4
t = 0.5 
theta = theta = np.linspace(0, 2 * np.pi, num=500, endpoint=True)
num_local = 1000
local_theta = np.linspace(0, 2 * np.pi, num=num_local, endpoint=False)





fig, ax = plt.subplots()
theta = np.linspace(0, 2 * np.pi, num=500, endpoint=True)

fireline_t0 = fire.compute_fireline_local(a, f, g, h, 0, theta, t_0)
ax.plot(fireline_t0[0], fireline_t0[1], 'b')
expected_fireline = fire.compute_fireline_local(a, f, g, h, 0, theta, t_0 + t)
ax.plot(expected_fireline[0], expected_fireline[1], 'r')



xdata, ydata = [], []
ln, = ax.plot([], [], 'g')

def init():
    return ln,

def update(frame):
    xdata = frame[0]
    ydata = frame[1]
    ln.set_data(xdata, ydata)
    return ln,

data = []
for theta_0 in local_theta:
    initial_point = fire.compute_fireline(a, f, g, h, theta_0, t_0)
    fireline_t = fire.compute_fireline_local(a, f, g, h, 0, theta, t, initial_point)
    data.append(fireline_t)
    
ani = FuncAnimation(fig, update, frames=data, init_func = init, blit=True, interval=10)