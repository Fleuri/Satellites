#!/usr/bin/python
from math import atan, cos, sin, tan
import numpy as np
import tokenize

def main():

    np.set_printoptions(threshold='nan')
    vector_array = dict();

    with open("data.txt") as file:
        lines = file.readlines();
        print "Satellites: \n"
        for line in lines:
            words = line.split(",");
            if (words.__len__()==4):
              vector_array[words[0]] = llarToWorld(float(words[1]), float(words[2]), float(words[3]))
            if (words.__len__()==5):
                print "Routes: \n"
                llarToWorld(float(words[1]), float(words[2]), 0)
                llarToWorld(float(words[3]), float(words[4]), 0)
        print vector_array.items()



def llarToWorld(lat, lon, alt, rad=6371/2):
    # see: http://www.mathworks.de/help/toolbox/aeroblks/llatoecefposition.html
    f  = 0                              # flattening
    ls = atan((1 - f)**2 * tan(lat))    # lambda

    x = rad * cos(ls) * cos(lon) + alt * cos(lat) * cos(lon)
    y = rad * cos(ls) * sin(lon) + alt * cos(lat) * sin(lon)
    z = rad * sin(ls) + alt * sin(lat)
    vector = np.array([x,y,z])
    print "vector"+ str(vector) + ","
    return vector

if __name__ == "__main__":
    main()
