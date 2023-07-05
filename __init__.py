from p5 import *
from Constants.elementary import * 
from computations.Particles import *

width = width
height = height

E_AMT = 50

def get_genXY():
   x = randomUniform(-width/2,width/2)
   y = randomUniform(-height/2,height/2)
   return x,y

particles = [Electron(*get_genXY()) for i in range(E_AMT)]
def setup():
   size(800, 800)
   no_stroke()
   fill(0)

def draw():
   background(255)
   translate(width/2,height/2)

   for idx in range(E_AMT):
      particles[idx].compute_force(particles,idx)
   for idx in range(E_AMT):
      circle((particles[idx].x,particles[idx].y),10)

if __name__ == '__main__':
   run()