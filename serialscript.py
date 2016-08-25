import serial
import time

commands = list()
counter = 0
iterator = 0
com = ""

#Function for reading module answers 
def answer():
    while ser.readline():
        print ser.readline()

com = raw_input("Enter the modem COM port number:")      
com = "COM" + com

#Get a list of commands
while 1:
    commands.append(raw_input("Enter a command:"))
    if commands[-1] == "":
        commands.pop()
        break
    counter += 1

#Open serial port
ser = serial.Serial(com, 115200, timeout=3)
if ser.is_open:
    pass
else:
    ser.open()

#Repeat AT commands repeatedly    
while 1:
    ser.write(commands[iterator])
    ser.write("\r\n")
    answer()
    iterator += 1
    if iterator >= counter:
        iterator = 0    
    time.sleep(5)

