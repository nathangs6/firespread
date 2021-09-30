# -*- coding: utf-8 -*-
"""
Title: fire.py
Author: Nathan Gurrin-Smith
Description: Contains the core functions for modeling wildfire spread using
Huygen's Principle
"""

import numpy as np

def compute_fireline(a, f, g, h, theta, t):
    return [a * t * f * np.cos(theta) + a * t * g, a * t * h * np.sin(theta)]


def compute_fireline_local(a, f, g, h, beta, theta, t, point=None):
    if point is None:
        point = np.array([0, 0])
    fireline_t = compute_fireline(a, f, g, h, theta, t)
    fireline_x = point[0] + fireline_t[0] * np.cos(beta) - fireline_t[1] * np.sin(beta)
    fireline_y = point[1] + fireline_t[0] * np.sin(beta) + fireline_t[1] * np.cos(beta)
    fireline_t = [fireline_x, fireline_y]
    return fireline_t

def compute_fireline_single(a, f, g, h, beta, theta, t):
    fireline_t = compute_fireline(a, f[0], g[0], h[0], theta, t[0])
    
    p = h[0] * np.cos(beta[1]) * np.cos(theta) + f[0] * np.sin(beta[1]) * np.sin(theta)
    q = h[0] * np.sin(beta[1]) * np.cos(theta) - f[0] * np.cos(beta[1]) * np.sin(theta)
    r = np.power(np.square(p) * f[1]**2 + np.square(q) * h[1]**2, -1/2)
    
    fireline_X = a * t[1] * (g[1] * np.cos(beta[1]) + r * (p * f[1]**2 * np.cos(beta[1]) + q * h[1]**2 * np.sin(beta[1])))
    fireline_Y = a * t[1] * (g[1] * np.sin(beta[1]) + r * (p * f[1]**2 * np.sin(beta[1]) - q * h[1]**2 * np.cos(beta[1])))
    
    fireline_t = fireline_t + np.array([fireline_X, fireline_Y])
    
    return fireline_t

