import serial
import time
from datetime import datetime
from openpyxl import Workbook
ser = serial.Serial('COM3', 9600) 

workbook = Workbook()
sheet = workbook.active

sheet.append(["Номер записи", "Время", "Температура (°C)", "Влажность воздуха(%)", "Влажность почвы(%)", "Интенсивность света(%)"])
num_record = 1 
while True:
 data = ser.readline().decode('utf-8').strip()
 print(num_record, data)
 current_time = datetime.now().strftime('%H:%M')
 temperature, humidity = data.split(',')
 sheet.append([num_record, current_time, float(temperature), float(humidity)])
 num_record += 1
 workbook.save('data.xlsx')
 time.sleep(5)