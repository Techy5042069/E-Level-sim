from constants.elementary import *
global width
global height

class Particle():
    def __init__(self,charge,mass,x,y,r):
        self.charge = charge #polarity: -1 -> electron 0-> neutron 1 -> proton
        self.mass = mass
        self.x = x
        self.y = y
        self.r = r
        self.Fx = 0
        self.Fy = 0
        self.Ax = 0
        self.Ay = 0
        self.Vx = 0
        self.Vy = 0
        # self.PrevE = 0
        # self.PE = 0

    def compute_force(self, particles: list, parIdx):
        for idx in range(parIdx + 1,len(particles)):
            par = particles[idx]
            distx = par.x - self.x
            disty = par.y - self.y
            dist = (distx ** 2 + disty ** 2) ** 0.5

            attractivity = 1 #attract
            if self.charge == par.charge:
                attractivity = -1 #repulsion
            elif self.charge == 0 or par.charge == 0:
                attractivity = 0
            newton_force_constant = GRAVITATIONAL_CONSTANT * self.mass * par.mass
            force_dist = (CFORCE_CONSTANT * attractivity  + newton_force_constant) / dist
            Fx = force_dist * distx/(dist ** 2)
            Fy = force_dist * disty/(dist ** 2)
            self.Fx += Fx
            self.Fy += Fy
            par.Fx += -Fx
            par.Fy += -Fy
            # self.PE += force_dist
        
        self.Ax = self.Fx/self.mass
        self.Ay = self.Fy/self.mass
        self.Vx += self.Ax
        self.Vy += self.Ay
        self.x += (self.Vx * PIXEL_FACTOR)
        self.y += (self.Vy * PIXEL_FACTOR)
        # tempV = self.Vx ** 2 + self.Vy ** 2
        # currE = self.mass * tempV - 2 * self.PE
        # diff = currE - self.PrevE
        # print("E_TRACK: ",self.charge, diff)
        # self.PrevE = currE
        # self.check_pos()

    def check_pos(self):
        if not (-width/2 < self.x < width/2) or not (-height/2 < self.y < height/2):
            self.x,self.y = get_genXY()
            self.Vx,self.Vy = 0,0
    def resetForces(self):
        self.Fx,self.Fy,self.PE = 0,0,0

class Proton(Particle):
    def __init__(self,x,y):
        super().__init__(1,PROTON_MASS,x,y,PROTON_RADIUS)


class Electron(Particle):
    def __init__(self,x,y):
        super().__init__(-1,ELECTRON_MASS,x,y,PROTON_RADIUS/ELECTRON_PROTON_FACTOR)
        # self.Vy  =  abs(self.x)/self.x* (FORCE_CONSTANT/(self.mass * 100)) ** 0.5 



from __init__ import get_genXY
