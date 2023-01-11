
import smbus
import time

DEVICE   = 0x36
POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07
bus = smbus.SMBus(1)

    
def main():
    print("Test Alpha")
    while(1):
        print("Test Bravo")
        feuchtLevel = readFeucht()
        print("test Charlie" + format(feuchtLevel, '.2f'))
        print(feuchtLevel)
        time.sleep(1)
        
def readFeucht(addr=DEVICE):
    print("Test Echo")
    data = bus.read_i2c_block_data(addr, 0x36)
    print(data)
    return convertToNumber(data)

def convertToNumber(data):
    result= (data[1] + (256*data[0]))
    return(result)

if __name__=="__main__":
    main()
