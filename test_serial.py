import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

print("Opened serial port")
time.sleep(2)

# arduino.write(b'1047\n')
notez = 440;
arduino.write(b'440\n')
arduino.flush()

print("Sent ")
print(notez)

time.sleep(1)

while arduino.in_waiting:
    print("Arduino:", arduino.readline().decode(errors="replace").strip())

arduino.close()