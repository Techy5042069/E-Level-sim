WIDTH,HEIGHT,THICKNESS = 1440,800,300
E_AMT = 1000
P_AMT = 0
N_AMT = 0


UNIFORM_SPREAD = 1 #1 if the initial state is going to be a regualr sphere/circle/square
SPREAD_RADIUS = 400  #for sphere/circle
SHAPE = 0 # 0 for sq, 1 for circle
UNIFROM_PAR_AMT = 10 # N number of particle per dimension, total par = N^k
K = 3 #dimension, k=2 for 2nd dim, 3 max, 2min
SEP = 50 #px, for square

EXTRA_SQUARE_OFFSET = UNIFROM_PAR_AMT/2 * SEP
DEFAULT_TRACKING_OFFSET = [WIDTH/2 ,HEIGHT/2]
if SHAPE == 0:
    DEFAULT_TRACKING_OFFSET[0] -= EXTRA_SQUARE_OFFSET
    DEFAULT_TRACKING_OFFSET[1] -= EXTRA_SQUARE_OFFSET

TRACKING = 0 #if you want to track nth particle
TRACKER = 126 #track N-1th particle , make sure to enable bg refresher

SAME_CHARGE_REPEL = -1 #1 for attraction, -1 for repulsion
TOTAL_UNUNIFORM = (E_AMT + P_AMT + N_AMT)
T_AMT = UNIFROM_PAR_AMT ** K if UNIFORM_SPREAD else TOTAL_UNUNIFORM