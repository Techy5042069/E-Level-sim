from p5 import *
from constants.elementary import * 
from computations.Particles import *
import numpy as np

WIDTH,HEIGHT = 800,800
E_AMT = 250
P_AMT = 250
def get_genXY():
   x = randomUniform(-WIDTH/2,WIDTH/2)
   y = randomUniform(-HEIGHT/2,HEIGHT/2)
   return x,y

particles = np.array([Electron(*get_genXY()) for i in range(E_AMT)] + [Proton(*get_genXY()) for i in range(P_AMT)])
# particles = np.array([Electron(125,300), Electron(-100,-150),Proton(100,100)])
T_AMT = particles.size
# particles = [Electron(*get_genXY()) for i in range(E_AMT)] + [Proton(*get_genXY()) for i in range(P_AMT)]
# print(particles.size)
def setup():
   size(WIDTH, HEIGHT)
   no_stroke()
   fill(0)
   background(255)



def draw():
   t1 = time.time()
   translate(WIDTH/2,HEIGHT/2)
   if mouse_is_pressed:
      background(255)
   for par in particles:
      par.resetForces()
   for idx in range(T_AMT):
      particles[idx].compute_force(particles,idx)
   for idx in range(T_AMT):
      col = "red" if particles[idx].charge == 1 else "blue"
      r = 25 if particles[idx].charge == 1 else 5
      fill(col)
      circle((particles[idx].x,particles[idx].y),r)
   print(time.time() - t1)

if __name__ == '__main__':
   # run(renderer="skia")
   run()