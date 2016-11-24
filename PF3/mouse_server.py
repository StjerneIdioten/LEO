import sys
import zmq
import struct

context = zmq.Context()
socket = context.socket(zmq.PUB)

#Setup port and ip
port = "5556"

if len(sys.argv) > 1:
    port = sys.argv[1]

socket.bind("tcp://*:" + port)

file = open( "/dev/input/mice", "rb" )

while True:

    buf = file.read(3);
    button = buf[0];
    bLeft = button & 0x1;
    bMiddle = (button & 0x4) > 0;
    bRight = (button & 0x2) > 0;
    x, y = struct.unpack("bb", buf[1:]);
    print("L:%d, M: %d, R: %d, x: %d, y: %d\n" % (bLeft, bMiddle, bRight, x, y));

    socket.send_string("10001 " + str(x) + ' ' + str(y))

file.close();