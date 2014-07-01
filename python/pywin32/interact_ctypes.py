import ctypes

def ctypes_click(x, y):
    ctypes.windll.user32.SetCursorPos(100, 20)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)

# broken :(
