
class LSystem2d:

    def __init__(self, axiom, rules, l_angle, r_angle, init_angle, d, x0, y0):
        self.axiom = axiom
        self.rules = rules
        self.l_angle = l_angle
        self.r_angle = r_angle
        self.init_angle = init_angle
        self.d = d
        self.x0 = x0
        self.y0 = y0
        
tree0 = LSystem2d('F', {'F':'F[+F]F[-F]F'}, 20, 20, 90, 3, 700, 50)
tree1 = LSystem2d('F', {'F':'F[+F]F[-F][F]'}, 30, 25.7, 90, 15, 700, 50)
tree2 = LSystem2d('F', {'F':'FF-[-F+F+F]+[+F-F-F]'}, 22.5, 22.5, 90, 5, 700, 50)
tree3 = LSystem2d('X', {'X':'F[+X]F[-X]+X','F':'FF'}, 20, 30, 90, 15, 700, 50)
tree4 = LSystem2d('X', {'X':'F[+X][-X]FX','F':'FF'}, 25.7, 25.7, 90, 15, 700, 50)
tree5 = LSystem2d('X', {'X':'F-[[X]+X]+F[+FX]-X','F':'FF'}, 25, 25, 110, 10, 700, 50)

koch = LSystem2d('F', {'F':'F+F--F+F'}, 60, 60, 0, 5, 200, 50)
koch90 = LSystem2d('F', {'F':'F+F-F-F+F'}, 90, 90, 0, 5, 200, 50)
sierpinski = LSystem2d('F-G-G', {'F':'F-G+F+G-F', 'G':'GG'}, 120, 120, 30, 20, 200, 400)

