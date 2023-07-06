from p5 import *
from constants.elementary import * 
from computations.Particles import *
import numpy as np

WIDTH,HEIGHT = 800,800
E_AMT = 1000

def get_genXY():
   x = randomUniform(-WIDTH/2,WIDTH/2)
   y = randomUniform(-HEIGHT/2,HEIGHT/2)
   return x,y

particles = np.array([Electron(*get_genXY()) for i in range(E_AMT)])
# particles = [Electron(*get_genXY()) for i in range(E_AMT)]

def setup():
   size(WIDTH, HEIGHT)
   no_stroke()
   fill(0)


def draw():
   background(255)
   translate(WIDTH/2,HEIGHT/2)
   t1 = time.time()
   for par in particles:
      par.resetForces()
   for idx in range(E_AMT):
      particles[idx].compute_force(particles,idx)
   for idx in range(E_AMT):
      circle((particles[idx].x,particles[idx].y),10)
   print(time.time() - t1)

if __name__ == '__main__':
   run(renderer="skia")
   # run()