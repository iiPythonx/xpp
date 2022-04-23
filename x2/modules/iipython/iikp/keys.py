# Keycodes
UP         = 72
DOWN       = 80
LEFT       = 75
RIGHT      = 77
ENTER      = 13
SPACE      = 32

INSERT     = 82
DELETE     = 83
HOME       = 71
END        = 79
PG_UP      = 73
PG_DOWN    = 81

ESCAPE     = 27
BACKSPACE  = 8

CTRL_C     = 3

# Function keys
F1         = 59
F2         = 60
F3         = 61
F4         = 62
F5         = 63
F6         = 64
F7         = 65
F8         = 66
F9         = 67
F10        = 68
F11        = 133
F12        = 134

# Key aliases
ESC        = ESCAPE
PAGE_DN    = PG_DOWN
PAGE_UP    = PG_UP
INS        = INSERT
DEL        = DELETE

# Keymap
MAP = [globals()[d] for d in globals() if not d.startswith("__") and d != "MAP" and isinstance(globals()[d], int)]
for _ in MAP:
    while MAP.count(_) > 1:
        MAP.remove(_)
