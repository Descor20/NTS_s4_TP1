
from mathsutils import *
from drawing.line import Line
from lsystems.lsystem2d import *
from lsystems.lsystem3d import *
import random

def derivation(axiom, rules):
    """
    axiom : string
    rules : dictionary
    return the result of the derivation
    """
    w = ""
    for elt in axiom :
        founder = False
        for key,value in rules.items() :
            if (key == elt) :
                w += value
                founder = True
        if not founder :
            w += elt
    return w;


def generation(axiom, rules, n):
    """
    axiom : string
    rules : dictionary
    n : integer
    return the result of n successive derivations
    """
    w = axiom
    for i in range(n) :
        w = derivation(w, rules)
    return w

def axiomtoline2d(gen : str, p : tuple[float, float], lsys : LSystem2d) -> list[Line]:
    def axiomtoline2(gen : str, p : tuple[float, float], lsys : LSystem2d) :
        line = []
        if (len(gen) == 0) :
            return line
        else :
            i = 0
            angle = lsys.init_angle
            nextc = (p[0], p[1])
            initc = (p[0], p[1])
            while (i < len(gen)) :
                if (gen[i] == 'F' or gen[i] == 'G') :
                    nextc = move2d(initc[0], initc[1], r2d(angle), lsys.d)
                    line.append(Line((initc[0], initc[1]),(nextc[0], nextc[1])))
                    initc = (nextc[0], nextc[1])
                elif (gen[i] == '+') :
                    angle += lsys.l_angle
                elif (gen[i] == '-') :
                    angle -= lsys.r_angle
                elif (gen[i] == '[') :
                    lsys.init_angle = angle
                    [l,ind] = axiomtoline2(gen[(i+1)::], [nextc[0], nextc[1]], lsys)
                    initc = nextc
                    i += ind + 1
                    for e in l :
                        line.append(e)
                elif (gen[i] == ']') :
                    return [line,i]
                i += 1
            return [line,i]
    l = axiomtoline2(gen, p, lsys)[0]
    return l

def axiomtoline3d(gen : str, p : tuple[float, float, float], lsys : LSystem3d) -> list[tuple[Line, int]]:
    def axiomtoline3(gen : str, p : tuple[float, float, float], lsys : LSystem3d, angle, depth) :
        line = []
        if (len(gen) == 0) :
            return line
        else :
            i = 0
            nextc = (p[0], p[1], p[2])
            initc = (p[0], p[1], p[2])
            while (i < len(gen)) :
                if (gen[i] == 'F' or gen[i] == 'G') :
                    nextc = move3d(initc[0], initc[1], initc[2], angle, lsys.d)
                    line.append((Line((initc[0], initc[1], initc[2]),(nextc[0], nextc[1], nextc[2])), depth))
                    initc = (nextc[0], nextc[1], nextc[2])
                elif (gen[i] == '+') :
                    angle = multmat(angle, ru3d(lsys.l_angle))
                elif (gen[i] == '-') :
                    angle = multmat(angle, ru3d(-lsys.r_angle))
                elif (gen[i] == '&') :
                    angle = multmat(angle, rl3d(lsys.d_angle))
                elif (gen[i] == 'ˆ') :
                    angle = multmat(angle, rl3d(-lsys.u_angle))
                elif (gen[i] == '>') :
                    angle = multmat(angle, rh3d(lsys.t_angle))
                elif (gen[i] == '<') :
                    angle = multmat(angle, rh3d(-lsys.v_angle))
                elif (gen[i] == '[') :
                    [l,ind] = axiomtoline3(gen[(i+1)::], [nextc[0], nextc[1], nextc[2]], lsys, angle, depth+1)
                    initc = nextc
                    i += ind + 1
                    for e in l :
                        line.append(e)
                elif (gen[i] == ']') :
                    return [line,i]
                i += 1
            return [line,i]
    angle = ru3d(lsys.init_angle)
    l = axiomtoline3(gen, p, lsys, angle, 0)[0]
    return l

def axiomtoline3drand(gen : str, p : tuple[float, float, float], lsys : LSystem3d, randmax : float) -> list[tuple[Line, int]]:
    pass
