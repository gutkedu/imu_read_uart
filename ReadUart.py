import serial
from datetime import datetime

ser = serial.Serial('COM3',921600)
ser.flushInput()

while True:
    try:
        #date = datetime.now().strftime("%Y%m%d%H%M%S")
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes.decode("utf-8")
        #decoded_bytes = float(decoded_bytes)
        #print(decoded_bytes)
        #data_string = date + "\t" + decoded_bytes
        data_string = decoded_bytes
        #print(data_string)
        with open('recorded_data', 'a') as data_file:
            data_file.write(data_string)
    except:
        print("Keyboard Interrupt")
        break

