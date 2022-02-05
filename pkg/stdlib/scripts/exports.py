# Variables
initialized = False
interpreter = None

# Functions
def init(x2):
    global initialized
    if not initialized:
        global interpreter
        interpreter = x2
        initialized = True
