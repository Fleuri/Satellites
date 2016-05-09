#!/usr/bin/python
from math import atan, cos, sin, tan
import numpy as np

def main():

    with open("data.txt") as file:
        print file.readlines()


def llarToWorld(lat, lon, alt, rad=6371):
    # see: http://www.mathworks.de/help/toolbox/aeroblks/llatoecefposition.html
    f  = 0                              # flattening
    ls = atan((1 - f)**2 * tan(lat))    # lambda

    x = rad * cos(ls) * cos(lon) + alt * cos(lat) * cos(lon)
    y = rad * cos(ls) * sin(lon) + alt * cos(lat) * sin(lon)
    z = rad * sin(ls) + alt * sin(lat)
    vector = np.array[x,y,z]
    print vector
    return vector

if __name__ == "__main__":
    main()
