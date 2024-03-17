import serial
ser = serial.Serial('COM3', 9600)
ser.write(b'Hello, Arduino!')
response = ser.readline()
decoded_response = response.decode('utf-8')
ser.close()
print(decoded_response)