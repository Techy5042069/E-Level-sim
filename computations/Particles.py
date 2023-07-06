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

    def compute_force(self, particles, parIdx):
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

            force_dist = FORCE_CONSTANT * attractivity / (dist ** 2) # F
            Fx = force_dist * distx/(dist)
            Fy = force_dist * disty/(dist)
            self.Fx += Fx
            self.Fy += Fy
            par.Fx += -Fx
            par.Fy += -Fy
        
        self.Ax = self.Fx/self.mass
        self.Ay = self.Fy/self.mass
        self.Vx += self.Ax
        self.Vy += self.Ay
        self.x += (self.Vx * PIXEL_FACTOR)
        self.y += (self.Vy * PIXEL_FACTOR)
        print("vel", self.Vx , self.Vy)
        print("pos",self.x , self.y)
        self.check_pos()

    def check_pos(self):
        if not (-width/2 < self.x < width/2) or not (-height/2 < self.y < height/2):
            self.x,self.y = get_genXY()
            self.Vx,self.Vy = 0,0
    def resetForces(self):
        self.Fx,self.Fy = 0,0

class Proton(Particle):
    def __init__(self,x,y):
        super().__init__(1,PROTON_MASS,x,y,PROTON_RADIUS)


class Electron(Particle):
    def __init__(self,x,y):
        super().__init__(-1,ELECTRON_MASS,x,y,PROTON_RADIUS/ELECTRON_PROTON_FACTOR)
        # self.Vy  =  abs(self.x)/self.x* (FORCE_CONSTANT/(self.mass * 100)) ** 0.5 



from __init__ import get_genXY
