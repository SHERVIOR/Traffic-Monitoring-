import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_read(l1, l2):
    combined_input = f"{l1},{l2}\n"
    arduino.write(bytes(combined_input, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    while True:
        try:
            l1 = int(input("Enter a value for L1: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            l2 = int(input("Enter a value for L2: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    value = write_read(l1, l2)
    print(value)