import smbus
import time

DEVICE   = 0x38
POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07
bus = smbus.SMBus(1)

def convertToNumber(data):
    result= (data[1] + (256*data[0])) /1.2
    return(result)

def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr, 0x20)
    return convertToNumber(data)

def main():
    while(1):
        lightLevel = readLight()
        print(format(lightLevel, '.2f')+ " lux")
        time.sleep(1)
if __name__=="__main__":
    main()