import pygame
from time import time,sleep
from setup import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def calc_dist(pos):
    frameDat[:, 0:3] = particles[:, 0:3] - pos
    frameDat[:, 4] = np.linalg.norm(frameDat[:, 0:3], 2, 1)
    # compute L2 norm


def det_attr(charge):
    frameDat[:, 3] = (particles[:, 3] * charge) * SAME_CHARGE_REPEL 


def calc_force(par, next_id):
    N_force = GRAVITATIONAL_CONSTANT * par[4] * particles[next_id:, 4]
    frameDat[next_id:, 5] = (CFORCE_CONSTANT * frameDat[next_id:, 3] + N_force) / (
        (frameDat[next_id:, 4] + (particles[next_id:,5] + par[5])/2) ** 3
    )


def get_dynamics(par, idx):
    fXYZ = frameDat[:, 0:3] * frameDat[:, 5][:, np.newaxis]
    if next_id := idx + 1 < len(particles):
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
        col, r = color_radius_map[par[3]]
        if idx == TRACKER: col = "green"
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
