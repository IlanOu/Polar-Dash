## SAVING IMAGE
STREAMING_ASSETS_PATH = "../StreamingAssets/photos"
MAX_IMAGE = 50

## CV2
WIDTH = 960
HEIGHT = 540

SCREEN_SEPARATOR = int(WIDTH/2)
LEFT_WIDTH = SCREEN_SEPARATOR
RIGHT_WIDTH = WIDTH - SCREEN_SEPARATOR


RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CARACTER_HEIGHT = 30
CARACTER_WIDTH = 20

# Coord of all MAIN SCREEN
TOP_LEFT_CORNER = ((0, 0), (int(WIDTH/3), int(HEIGHT/3)))
TOP_RIGHT_CORNER = ((int(2*WIDTH/3), 0), (WIDTH, int(HEIGHT/3)))
BOT_LEFT_CORNER = ((0, int(2*HEIGHT/3)), (int(WIDTH/3), HEIGHT))
BOT_RIGHT_CORNER = ((int(2*WIDTH/3), int(2*HEIGHT/3)), (WIDTH, HEIGHT))
CENTER = ((int(WIDTH/3), int(HEIGHT/3)), (int(2*WIDTH/3), int(2*HEIGHT/3)))

## DETECTION
# ATTENTION LES DONNEES DROITE/GAUCHE SONT INVERSE
SHOW_BONES = True
NOSE = 0
RIGHT_SHOULDER = 11
LEFT_SHOULDER = 12
RIGHT_WRIST = 15
LEFT_WRIST = 16
RIGHT_INDEX = 19
LEFT_INDEX = 20
RIGHT_HIP = 23
LEFT_HIP = 24
RIGHT_KNEE = 25
LEFT_KNEE = 26
RIGHT_ANKLE = 27
LEFT_ANKLE = 28

## CONFIG
IS_SOLO_PLAYER = False
SOLO_PLAYER = "LEFT"
ANALYSE_DURATION = 1 # Seconds
COEF_SQUAT_RANGE = 2
COEF_JUMP_RANGE = 3
COEF_TOP_RANGE = 0.8
COEF_BOTTOM_RANGE = 1.2
COEF_LEFT_RANGE = 0.7
COEF_RIGHT_RANGE = 0.7

DEFAULT_JUMP_RANGE = 50
DEFAULT_SQUAT_RANGE = 100

DEFAULT_RANGE_TOP_SQUARE = 170
DEFAULT_RANGE_BOTTOM_SQUARE = 100
DEFAULT_RANGE_LEFT_SQUARE = 120
DEFAULT_RANGE_RIGHT_SQUARE = 120


# ZONE COORD
# [LEFT/RIGHT][FIRST/SECOND POINT][X/Y]
DEFAULT_SQUARE_HEIGHT = 100
DEFAULT_SQUARE_WIDTH = 100

INITIAL_TOP_AREA = [[[0, 0], [LEFT_WIDTH, DEFAULT_SQUARE_HEIGHT]], [[0, 0], [RIGHT_WIDTH, DEFAULT_SQUARE_HEIGHT]]]
INITIAL_BOTTOM_AREA = [[[0, HEIGHT - DEFAULT_SQUARE_HEIGHT], [LEFT_WIDTH, HEIGHT]], [[0, HEIGHT - DEFAULT_SQUARE_HEIGHT], [RIGHT_WIDTH, HEIGHT]]]
INITIAL_LEFT_AREA = [[[0, 0], [DEFAULT_SQUARE_WIDTH, HEIGHT]], [[0, 0], [DEFAULT_SQUARE_WIDTH, HEIGHT]]]
INITIAL_RIGHT_AREA = [[[LEFT_WIDTH - DEFAULT_SQUARE_WIDTH, 0], [LEFT_WIDTH, HEIGHT]], [[RIGHT_WIDTH - DEFAULT_SQUARE_WIDTH, 0], [LEFT_WIDTH, HEIGHT]]]


# DYNAMICS VARIABLES

LEFT_JUMP_RANGE = DEFAULT_JUMP_RANGE
LEFT_SQUAT_RANGE = DEFAULT_SQUAT_RANGE

RIGHT_JUMP_RANGE = DEFAULT_JUMP_RANGE
RIGHT_SQUAT_RANGE = DEFAULT_SQUAT_RANGE

LEFT_RANGE_TOP_SQUARE = DEFAULT_RANGE_TOP_SQUARE
LEFT_RANGE_BOTTOM_SQUARE = DEFAULT_RANGE_BOTTOM_SQUARE
LEFT_RANGE_LEFT_SQUARE = DEFAULT_RANGE_LEFT_SQUARE
LEFT_RANGE_RIGHT_SQUARE = DEFAULT_RANGE_RIGHT_SQUARE

RIGHT_RANGE_TOP_SQUARE = DEFAULT_RANGE_TOP_SQUARE
RIGHT_RANGE_BOTTOM_SQUARE = DEFAULT_RANGE_BOTTOM_SQUARE
RIGHT_RANGE_LEFT_SQUARE = DEFAULT_RANGE_LEFT_SQUARE
RIGHT_RANGE_RIGHT_SQUARE = DEFAULT_RANGE_RIGHT_SQUARE

def resetSquare():
    global TOP_AREA, BOTTOM_AREA, LEFT_AREA, RIGHT_AREA
    TOP_AREA = INITIAL_TOP_AREA
    BOTTOM_AREA = INITIAL_BOTTOM_AREA
    LEFT_AREA = INITIAL_LEFT_AREA
    RIGHT_AREA = INITIAL_RIGHT_AREA

resetSquare()

