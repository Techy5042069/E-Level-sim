from Constants.elementary import * 
import math
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
        self.Fx = 0
        self.Fy = 0
    
        for idx,par in enumerate(particles):
            if idx == parIdx: continue

            distx = par.x - self.x
            disty = par.y - self.y
            angle = math.atan2(disty,distx)
            dist = distx ** 2 + disty ** 2
            attractivity = 1 #attract
            if self.charge == par.charge:
                attractivity = -1 #repulsion
            elif self.charge == 0 or par.charge == 0:
                attractivity = 0
            force = COLUMB_CONSTANT * CHARGE**2 * attractivity / dist
            self.Fx += force * math.cos(angle)
            self.Fy += force * math.sin(angle)
        
        self.Ax = self.Fx/ELECTRON_MASS
        self.Ay = self.Fy/ELECTRON_MASS
        self.Vx += self.Ax
        self.Vy += self.Ay
        self.x += self.Vx
        self.y += self.Vy
        self.check_pos()

    def check_pos(self):
        if not (-width/2 < self.x < width/2) or not (-height/2 < self.y < height/2):
            pass

class Electron(Particle):
    def __init__(self,x,y):
        super().__init__(-1,ELECTRON_MASS,x,y,ELECTRON_RADIUS)