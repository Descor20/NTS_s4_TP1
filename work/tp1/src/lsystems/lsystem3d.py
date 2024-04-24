
class LSystem3d:

    def __init__(self, axiom, rules, l_angle, r_angle, u_angle, d_angle, t_angle, v_angle, init_angle, ratio, d):
        self.axiom = axiom
        self.rules = rules
        self.l_angle = l_angle
        self.r_angle = r_angle
        self.d_angle = d_angle
        self.u_angle = u_angle
        self.t_angle = t_angle
        self.v_angle = v_angle
        self.init_angle = init_angle
        self.ratio = ratio
        self.d = d
        

tree3d0 = LSystem3d('T', {'T':'TF', 'F':'F[+F][-FF][<F][>FF][&F]'}, 45, 45, 50, 40, 30, 30, 90, 1.5, 40)
tree3d1 = LSystem3d('F', {'F':'IFF[Y-FF][Y+FF][Y<FF][Y>FF]'}, 40, 40, 40, 40, 20, 20, 90, 1.5, 40)


