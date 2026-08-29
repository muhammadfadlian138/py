from flask import Flask, render_template
import serial
import time

app = Flask(__name__)

# arduino = serial.Serial('/dev/ttyACM0', 9600)
# arduino = serial.Serial('/dev/ttyUSB0', 9600)
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

time.sleep(2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play/<int:frequency>")
def play(frequency):
    print(f"Sending: {frequency}")

    arduino.write(f"{frequency}\n".encode())
    arduino.flush()

    print("Sent!")

    return f"Playing {frequency} Hz"

@app.route("/stop")
def stop():
    arduino.write(b"0\n")
    arduino.flush()

    return "Stopped"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)