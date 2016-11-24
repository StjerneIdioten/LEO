from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
m.click(int(x_dim/2), int(y_dim/2), 1)
m.move(20, 20)
k.type_string('Hello, World!')