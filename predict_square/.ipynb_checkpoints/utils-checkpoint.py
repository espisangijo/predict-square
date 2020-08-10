import numpy as np
from typing import List, Set, Dict
from scipy import interpolate as inp

def __normalize_data(data, mx, mn):
    mx = mx - mn
    data = [(d - mn) / mx for d in data]

    return data

def normalize(data):
    max_time, max_x, max_y = -1, -1, -1
    time_data, x_data, y_data = [], [], []
    for time, x, y in data:
        time_data.append(time)
        x_data.append(x)
        y_data.append(y)
    max_time, min_time = max(time_data), min(time_data)
    max_x, min_x = max(x_data), min(x_data)
    max_y, min_y = max(y_data), min(y_data)

    normalized_data = list(zip(__normalize_data(time_data, max_time, min_time), __normalize_data(x_data, max_x, min_x), __normalize_data(y_data, max_y, min_y)))
    return normalized_data

def interpolate(data, div):
    time_data, x_data, y_data = [],[],[]
    for time, x, y in data:
        time_data.append(time)
        x_data.append(x)
        y_data.append(y)

    step = (max(time_data) - min(time_data)) / div

    fx = inp.interp1d(time_data, x_data)
    fy = inp.interp1d(time_data, y_data)

    points = np.arange(min(time_data), max(time_data), step)
    xnew = fx(points)
    ynew = fy(points)

    return list(zip(xnew, ynew))

def skinny(data):
    a, b = [], []
    for x, y in data:
        a.append(x)
        b.append(y)
    return list(a) + list(b)