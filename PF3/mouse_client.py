import sys
import zmq
from pymouse import PyMouse

#Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

#Setup mouse
m = PyMouse()

#Setup port and ip
port = "5556"
ip = "localhost"

if len(sys.argv) > 1:
    ip = sys.argv[1]

if len(sys.argv) > 2:
    port = sys.argv[2]


print("Collecting mouse data from " + ip + ":" + port)
socket.connect("tcp://" + ip + ":" + port)

topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

while True:
    string = socket.recv_string()
    topicfilter, x, y = string.split()
    print("x: " + x + ", y: " + y)
    xM,yM = m.position()
    m.move(xM + int(x), yM - int(y))