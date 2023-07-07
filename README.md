# E-Level-Sim (Electron-Level-Sim)

## Objective:
    * To simulate real physics
    * To simulate life
    * To understand and create what's called, us.
    * And use up a bunch of that juiccy computational power.


## requirements:
    * constraints(constants eg Gravitational constant)
    * functions

## Description:
    **life is limitless** or so it is said. 

    A computer processes data in frames. For example, a game is not updated infinitely in a discrete time frame.
    So, the actual simulation will somewhat differ from the reality -- given that all the constraints are accurate and precise -- because Time isn't a discrete value.

    But having a low update time (related to Frames per second) might lead to Tunnelling(google: CCD tunneling), and deviation from what should be actually happening.

    One way to fix this is the highest speed possible(in classical physics), `c = 3 * 10^8 m/s`. This means if we process each frame every `1/c` seconds we should be able to acheive the optimium result, But  this also means we have to process `30million` frames to get a second of result. So this is an important and interesting aspect of this project which we will compare with different values.

## The Mathematics

    Given a specific set of position of `N` particles, each particle experiences `N-1` forces from other particles whether that'd be a Columb Force or a Newtonian Force.

    The resultant of the forces is going to be the vector sum of `p * (N-1)` vectors where p is the type of forces.

    1 px = 1 m

    there are various models that describe particles and their nature:
        1. Bohr's model
        2. Bohr's model combined with the wave nature of electron
        3. Eliptical orbit nature of Electron
        4. Orbital theory
        5. Super position of Energy theory
    