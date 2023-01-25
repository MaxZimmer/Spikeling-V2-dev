import sys
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo

BaudRate = 115200

def COM():
    portList = []
    ports = QSerialPortInfo().availablePorts()
    for port in ports:
        if sys.platform == "linux" or sys.platform == "linux2":
            portList.append(port.systemLocation())
            print(port.systemLocation())
        else:
            portList.append(port.portName())
    return ports


DarkSolarized = [[11, 30, 38], [0, 43, 54], [7, 54, 66],                                           # 0:DarkBase01, 1:DarkBase02, 2:DarkBase03
                 [220, 50, 47], [133, 153, 0], [38, 139, 210],                                     # 3:Red, 4:Green, 5:Blue
                 [203, 75, 22], [42, 161, 152], [181, 137, 0], [108, 113, 196], [211, 54, 130],    # 6:Orange, 7:Cyan, 8:Yellow, 9:Violet, 10:Magenta
                 [88, 110, 117], [101, 123, 131], [131, 148, 150], [147, 161, 161],                # 11:Content01, 12:Content02, 13:Content03, 14:Content04
                 [238, 232, 213],[253, 246, 227]]                                                  # 15:LightBase01, LightBase02              # 15:LightBase01, LightBase02





