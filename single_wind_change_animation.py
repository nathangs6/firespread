"""
Title: single_wind_change_animation.py
Author: Nathan Gurrin-Smith
Description: Animation for a single wind change
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import fire


a = 1
f_old = 2
g_old = 0.5
h_old = 1
t_0 = 4

f_new = 5
g_new = 3
h_new = 2
beta = np.pi / 4
t = 0.5


theta = theta = np.linspace(0, 2 * np.pi, num=500, endpoint=True)
num_huygen = 1000
huygen_theta = np.linspace(0, 2 * np.pi, num=num_huygen, endpoint=False)


# Generate Data



initial_fireline = fire.compute_fireline(a, f_old, g_old, h_old, theta, t_0)


expected_fireline = fire.compute_fireline_single(a, [f_old, f_new], [g_old, g_new], [h_old, h_new], [0, beta], theta, [t_0, t])


xmin = np.amin(expected_fireline[0])
xmax = np.amax(expected_fireline[0])
ymin = np.amin(expected_fireline[1])
ymax = np.amax(expected_fireline[1])




data = []
for theta_0 in huygen_theta:
    initial_point = fire.compute_fireline_local(a, f_old, g_old, h_old, 0, theta_0, t_0)
    fireline_t = fire.compute_fireline_local(a, f_new, g_new, h_new, beta, theta, t, initial_point)
    data.append(fireline_t)


# Generate initial plot

fig, ax = plt.subplots()
ax.set_xlim([xmin - 1, xmax + 1])
ax.set_ylim([ymin - 1, ymax + 1])
ax.set_title("Single Wind Change")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()



ax.plot(initial_fireline[0], initial_fireline[1], 'b', label="First Fireline")
ax.plot(expected_fireline[0], expected_fireline[1], 'r', label="Second Fireline")

# Make animation

xdata, ydata = [], []
ln, = ax.plot([], [], 'g', label="Huygen Spread")

def init():
    return ln,

def update(frame):
    xdata = frame[0]
    ydata = frame[1]
    ln.set_data(xdata, ydata)
    return ln,


ax.legend()
ani = FuncAnimation(fig, update, frames=data, init_func = init, blit=True, interval=10)

