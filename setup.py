from constants.elementary import *
import numpy as np
from modes import *
import itertools

color_radius_map = {-1: ("blue", 2), 0.0: ("yellow", 8), 1: ("red", 8)}


def get_genXYZ():
    x = np.random.uniform(-WIDTH/2, WIDTH/2)
    y = np.random.uniform(-HEIGHT/2, HEIGHT/2)
    z = np.random.uniform(-THICKNESS/2, THICKNESS/2)
    return x, y, z

mass_radius_map = {
    -1: [ELECTRON_MASS, ELECTRON_RADIUS],
    0: [NEUTRON_MASS, NEUTRON_RADIUS],
    1: [PROTON_MASS, PROTON_RADIUS],
}


def get_par_values():
    global cE_AMT, cP_AMT, cN_AMT
    if cE_AMT > 0:
        cE_AMT -= 1
        c = -1
    elif cP_AMT > 0:
        cP_AMT -= 1
        c = 1
    else:
        cN_AMT -= 1
        c = 0
    arr = mass_radius_map[c]
    return c, *arr


#make another for planar
def gen_spherical_points(): 
    for i in range(UNIFROM_PAR_AMT):
        rot = np.random.uniform(0,2 * np.pi) if K == 3 else 0
        rot_factor = np.cos(rot)
        x = SPREAD_RADIUS * np.exp(complex(0,2*np.pi * i/UNIFROM_PAR_AMT))
        yield x.real * rot_factor,x.imag * rot_factor, SPREAD_RADIUS * np.sin(rot)

        #basically, (x,y,z) = R *(cosA * cosB , sinA * cos B , sinB)
        #projection rotation wrt to xy (A) and z,xy-plane(B)

def gen_square_points(coords):
     c = [coords[0] * SEP,coords[1] * SEP,0]
     if len(coords) == 3:
         c[2] = coords[2] * SEP
     return c

if UNIFORM_SPREAD:
    if SHAPE: #sphere
        cE_AMT = T_AMT
        spherical = gen_spherical_points()
        particles = np.array(
            [[*coords, *get_par_values(), 0, 0, 0, 0, 0, 0] for coords in spherical],
        )
    else:   #square
        cE_AMT = T_AMT ** K
        particles = np.array(
            [[*gen_square_points(coords), *get_par_values(), 0, 0, 0, 0, 0, 0] for coords in itertools.product(range(UNIFROM_PAR_AMT),repeat=K )],
        )

else: #random spread
    cE_AMT, cP_AMT, cN_AMT = E_AMT,P_AMT,N_AMT
    particles = np.array(
        [[*get_genXYZ(), *get_par_values(), 0, 0, 0, 0, 0, 0] for i in range(T_AMT)],
        dtype=float,
    )

frameDat = np.array([[0, 0, 0, 0, 0, 0] for i in range(len(particles))], dtype=float)
print(frameDat.shape)
# [[x,y,z],[c,m,r],[Vx,Vy,Vz],[xFx,xFy,xFz]]
# every particle Data
# xF => precalculated force from previous calculation to reduce time complexity from O(N^2) to O(N log N)
# every particle data against one, refreshed N times for one frame, N = no. of particles
# [[distx,disty,distz],attr,dist,F/d^3,[Fx,Fy,Fz]]