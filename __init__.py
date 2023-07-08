from p5 import *
from constants.elementary import * 
# from computations.Particles import *
import numpy as np
from timeit import timeit

WIDTH,HEIGHT = 800,800
E_AMT = 500
P_AMT = 500
cE_AMT = E_AMT
cP_AMT = P_AMT
T_AMT = E_AMT + P_AMT

def get_genXYZ() -> list[int]:
   x = randomUniform(-WIDTH/2,WIDTH/2)
   y = randomUniform(-HEIGHT/2,HEIGHT/2)
   z = randomUniform(-100,100)
   return x,y,z

def get_getCharge():
   return [1]

def get_par_values():
   # c = np.random.choice([-1,1],size=1)[0]
   global cE_AMT,cP_AMT
   if cE_AMT > 0:
      cE_AMT -= 1
      c = -1
   else:
      cP_AMT -= 1
      c = 1
   m = ELECTRON_MASS if c == -1 else PROTON_MASS
   r = ELECTRON_PROTON_FACTOR if c == -1 else PROTON_RADIUS
   return c,m,r

particles = np.array([
   [*get_genXYZ(),*get_par_values(),0,0,0,0,0,0,0,0] for i in range(T_AMT)
],dtype=float)
print(particles)
frameDat = np.array([
   [0,0,0,0,0,0,0,0,0] for i in range(T_AMT)
],dtype=float)


#[[x,y,z],[c,m,r],[Vx,Vy,Vz],[xFx,xFy,xFz]]

# xF => precalculated force from previous calculation to reduce time complexity from O(N^2) to O(N log N)

# [[distx,disty,distz],attr,dist,F/d^3,[Fx,Fy,Fz]]



def calc_dist(pos):
   frameDat[:,0:3] = particles[:,0:3] - pos
   frameDat[:,4] = np.linalg.norm(frameDat[:,0:3],2,1)
   #compute L2 norm

def det_attr(charge):
   # frameDat[:,3] = np.array([-1 if c == charge else 1 if c != charge else 0 for c in particles[:,3]])
   frameDat[:,3] = (particles[:,3] * charge) * -1

def calc_force(par,idx):
   N_force = GRAVITATIONAL_CONSTANT * par[4] * particles[idx:,4]
   # N_force = 0
   frameDat[idx:,5] += (CFORCE_CONSTANT * frameDat[idx:,3] + N_force) / (frameDat[idx:,4] ** 3)

def get_dynamics(par,idx):
   fXYZ = np.array([(frameDat[:,0] * frameDat[:,5]),(frameDat[:,1] * frameDat[:,5]),(frameDat[:,2] * frameDat[:,5])]) 
   dV = (np.sum(fXYZ,1) - par[9:12])/par[4]
   if idx < T_AMT:
      particles[idx,9:12] = fXYZ.transpose()[1] 
   return dV

def setup():
   size(WIDTH, HEIGHT)
   no_stroke()
   fill(0)
   background(255)

frames = 0
def draw():
   t1 = time.time()
   global frames
   frames += 1
   # translate(WIDTH/2,HEIGHT/2)
   background(255)
   # if mouse_is_pressed:
   idx = 0
   for par in particles:
      frameDat[:,5] = 0
      calc_dist(par[0:3]) #calc dx,dy,dz,d
      det_attr(par[3])  #calc attar
      calc_force(par,idx + 1) 
      deltaVel = get_dynamics(par,idx + 1)
      particles[idx,6:9] += deltaVel
      idx +=1

   particles[:,0:3] += particles[:, 6:9]
   # print('***************************************************************')
   # print(*particles[:,:],sep='\n\n')
   # print('***************************************************************\n')
   for par in particles:
      # disp_par(par)
      col = "red" if par[3] == 1 else "blue"
      r = 25 if par[3] == 1 else 5
      fill(col)
      circle(par[0:2],r)
   print(time.time() - t1)


if __name__ == '__main__':
   # deltaT = timeit(lambda: run(renderer="skia"),number=1)
   run(renderer="skia")
   # run()
# deltaT = time.time() - t1
print("frames: ", frames)
# print("Time: ", deltaT )
# print("FPS: ", frames/deltaT)

