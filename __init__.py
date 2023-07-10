import numpy as np
import pygame
from constants.elementary import *
from modes import *
from time import time
import itertools

cE_AMT = E_AMT
cP_AMT = P_AMT
cN_AMT = N_AMT
T_AMT = E_AMT + P_AMT + N_AMT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def get_genXYZ():
    x = np.random.uniform(0, WIDTH)
    y = np.random.uniform(0, HEIGHT)
    z = np.random.uniform(0, THICKNESS)
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

if UNIFORM_SPREAD:
    particles = np.array(
        [[*(c * SEP for c in coords), *get_par_values(), 0, 0, 0, 0, 0, 0] for coords in itertools.product(range(PAR_AMT_PER_DIM),repeat=K )],
    )
else:
    particles = np.array(
        [[*get_genXYZ(), *get_par_values(), 0, 0, 0, 0, 0, 0] for i in range(T_AMT)],
        dtype=float,
    )


frameDat = np.array([[0, 0, 0, 0, 0, 0] for i in range(T_AMT)], dtype=float)

# [[x,y,z],[c,m,r],[Vx,Vy,Vz],[xFx,xFy,xFz]]
# every particle Data
# xF => precalculated force from previous calculation to reduce time complexity from O(N^2) to O(N log N)
# every particle data against one, refreshed N times for one frame, N = no. of particles
# [[distx,disty,distz],attr,dist,F/d^3,[Fx,Fy,Fz]]

# display color and radius vals
color_radius_map = {-1: ("blue", 2), 0.0: ("yellow", 8), 1: ("red", 8)}


def calc_dist(pos):
    frameDat[:, 0:3] = particles[:, 0:3] - pos
    frameDat[:, 4] = np.linalg.norm(frameDat[:, 0:3], 2, 1)
    # compute L2 norm


def det_attr(charge):
    frameDat[:, 3] = (particles[:, 3] * charge) * -1


def calc_force(par, next_id):
    N_force = GRAVITATIONAL_CONSTANT * par[4] * particles[next_id:, 4]
    frameDat[next_id:, 5] = (CFORCE_CONSTANT * frameDat[next_id:, 3] + N_force) / (
        (frameDat[next_id:, 4] + (particles[next_id:,5] + par[5])/2) ** 3
    )


def get_dynamics(par, idx):
    fXYZ = frameDat[:, 0:3] * frameDat[:, 5][:, np.newaxis]
    if next_id := idx + 1 < T_AMT:
        particles[next_id:, 9:12] += fXYZ[next_id:, :]
    return (np.sum(fXYZ, 0) - particles[idx, 9:12]) / par[4]  # dV -> a


frame = 1
while 1:
    particles[:, 9:12] = 0
    idx = 0
    screen.fill("BLACK")
    t1 = time()

    for par in particles:
        frameDat[:, 5] = 0
        calc_dist(par[0:3])  # calc dx,dy,dz,d
        det_attr(par[3])  # calc attaractivity
        calc_force(par, idx + 1)
        deltaVel = get_dynamics(par, idx)
        particles[idx, 6:9] += deltaVel
        idx += 1

    particles[:, 0:3] += particles[:, 6:9]
    idx = 0

    for par in particles:
        # if par[3] != -1:
            # continue  # skip rendering if the paraticle isn't electron
        col, r = color_radius_map[par[3]]
        if idx == TRACKER:
            col = "green"
        pygame.draw.circle(
            screen,
            col,
            (
                par[0:2]
                + DEFAULT_TRACKING_OFFSET
                + (-particles[TRACKER, 0:2] if TRACKING else [0, 0])
            ),
            r,
        )
        idx += 1

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

    print(time() - t1)
