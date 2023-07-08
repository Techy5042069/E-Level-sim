from p5 import *
from constants.elementary import * 
# from computations.Particles import *
import numpy as np
import timeit

WIDTH,HEIGHT = 800,800
E_AMT = 5
P_AMT = 0
T_AMT = E_AMT + P_AMT
def get_genXYZ() -> list[int]:
   x = randomUniform(-WIDTH/2,WIDTH/2)
   y = randomUniform(-HEIGHT/2,HEIGHT/2)
   z = randomUniform(-100,100)
   return x,y,z
def get_getCharge():
   return np.random.choice([-1,1],size=1)


# particles = np.array([Electron(*get_genXY()) for i in range(E_AMT)] + [Proton(*get_genXY()) for i in range(P_AMT)])
# particles = np.array([Electron(125,300), Electron(-100,-150),Proton(100,100)])
particles = np.array([
   [*get_genXYZ(),get_getCharge(),1,1,0,0,0,0,0,0,0,0,0,0] for i in range(T_AMT)
],dtype=float)

frameDat = np.array([
   [0,0,0,0,0] for i in range(T_AMT)
],dtype=float)


print(particles)
# particles = np.array([-1,0,0,0,1,1,2,3,4])
#[[x,y,z],[c,m,r],[Fx,Fy,Fz],[Vx,Vy,Vz]]
# [distx,disty,distz,attr,dist]

# particles = [Electron(*get_genXY()) for i in range(E_AMT)] + [Proton(*get_genXY()) for i in range(P_AMT)]
# print(particles[:,6:9])
# particles[:,6:9] = 34
# print(particles) 40000> 118


def calc_dist(pos):
   frameDat[:,0:3]=particles[:,0:3] - pos
   frameDat[:,4] = np.linalg.norm(frameDat[:,0:3],2,1)
   #compute L2 norm
   print(frameDat)
def det_attr(charge):
   # frameDat[:,3] = -1 if particles[:,3] == charge else 1 if particles[:,3] != charge else 0
   # res = [charge == p_charge for p_charge in frameDat[:,3]]
   for c in frameDat[:,3]:
      # print(type(c))
      print(c == charge)
   # print(res)


def setup():
   size(WIDTH, HEIGHT)
   no_stroke()
   fill(0)
   background(255)

def draw():
   translate(WIDTH/2,HEIGHT/2)
   if mouse_is_pressed:
      background(255)
   t1 = time.time()
   # for par in particles:
   #    par.resetForces()
   particles[:,6:9] = 0 #reset previous forces
   # for idx in range(T_AMT):
   #    particles[idx].compute_force(particles,idx)
   for par in particles:
      calc_dist(par[0:3]) #calc dx,dy,dz,d
      det_attr(par[3])
      



   exit()
   # for idx in range(T_AMT):
   #    col = "red" if particles[idx].charge == 1 else "blue"
   #    r = 25 if particles[idx].charge == 1 else 5
   #    fill(col)
   #    circle((particles[idx].x,particles[idx].y),r)
   # print(time.time() - t1)

if __name__ == '__main__':
   # run(renderer="skia")
   run()