from math import pi, cos, sin
from random import randint


def degreetorad(theta):
    """
    theta : float
    return the conversion in radian
    """
    return (theta * (pi / 180))

def multmatvector(M: list[list[float]], X: list[float]):
    """
    M : matrix of size n * m
    X : vector of size m
    return the product of M and X
    """
    L = []
    for i in range(len(M)):
        res = 0
        for j in range(len(M[i])):
            res += M[i][j] * X[j]
        L.append(res)
    return L

def multmat(M1: list[list[float]], M2: list[list[float]]):
    """
    M1 : matrix of size n * m
    M2 : matrix of size m * p
    return the product of M1 and M2
    """
    L=[]
    for i in range(len(M1)):
        l = []
        for j in range(len(M2[0])):
            res = 0
            for k in range (len(M2)) :
                res += M2[k][j] * M1[i][k]
            l.append(res)
        L.append(l)
    return L

def r2d(theta):
    """
    theta : angle in degrees
    return the 2d rotation matrix of angle theta
    """
    rad = degreetorad(theta)
    a1 = cos(rad)
    a2 = -sin(rad)
    b1 = sin(rad)
    b2 = cos(rad)
    return [[a1,a2],[b1,b2]]

def move2d(x, y, r, d):
    """
    x, y : initial position
    r : rotation matrix representing the current direction
    d : distance
    return the new coordinates
    """
    temp = multmatvector(r, [d, 0])
    L = []
    base = [x, y]
    l = []
    for i in range(2) :
        l.append(base[i] + temp[i])
    return (l[0], l[1])
    
def ru3d(theta):
    """
    theta : angle in degrees
    return the 3d rotation matrix of angle theta along the axis ru
    """
    ang = degreetorad(theta)
    return [[cos(ang), -sin(ang), 0],[sin(ang), cos(ang), 0], [0, 0, 1]]
    
def rl3d(theta):
    """
    theta : angle in degrees
    return the 3d rotation matrix of angle theta along the axis rl
    """
    ang = degreetorad(theta)
    return [[1, 0, 0],[0, cos(ang), -sin(ang)],[0, sin(ang), cos(ang)]]
    
def rh3d(theta):
    """
    theta : angle in degrees
    return the 3d rotation matrix of angle theta along the axis rh
    """
    ang = degreetorad(theta)
    return [[cos(ang), 0, sin(ang)],[0, 1, 0],[-sin(ang), 0, cos(ang)]]

def move3d(x, y, z, r, d):
    """
    x, y, z : initial position
    r : rotation matrix representing the current direction
    d : distance
    return the new coordinates
    """
    temp = multmatvector(r, [d, 0, 0])
    l = []
    base = [x, y, z]
    for i in range(3) :
        l.append(base[i] + temp[i])
    return (l[0], l[1], l[2])

