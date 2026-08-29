import serial
import time
import turtle

n = 0;

turtle.penup();
turtle.goto(-600,200);
turtle.pendown();

def lirik(l,w):
    global n;
    print(l, end="", flush=True);
    turtle.write(l);
    turtle.goto(n*20, 200);
    time.sleep(w);
    n = n+1;

turtle.forward(90);
arduino = serial.Serial('/dev/ttyUSB0', 9600);
time.sleep(1.75);
offs = -0.15

lirik("Hi",     0.5     +offs);
lirik("dup",    0.5     +offs);
lirik("ku",     0.5     +offs);
lirik(" tan",   1.5     +offs);
lirik("pa",   0.5       +offs);
lirik(" cin",   1.25    +offs);
lirik("ta",   0.5       +offs);
lirik("mu\n",   0.5     +offs);
time.sleep(2.25);
lirik("Ba",   0.5       +offs);
lirik("gai ",   0.5     +offs);
lirik("ma",   0.5       +offs);
lirik("lam",   0.5      +offs);
lirik(" tan",   1.5     +offs);
lirik("pa ",   0.5      +offs);
lirik("Bin",   0.5      +offs);
lirik("tang",   0.5     +offs);

# time.sleep(2);

# else :
#     print("no")

# time.sleep(2)

# arduino.write(b'440\n')
# time.sleep(1)

# arduino.write(b'523\n')
# time.sleep(1)

# arduino.write(b'0\n')

turtle.done();
arduino.close();