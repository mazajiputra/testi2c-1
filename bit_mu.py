#!/usr/bin/python

import smbus

class multiplex:
    
    def __init__(self, bus):
        self.bus = smbus.SMBus(bus)

    def channel(self, address=0x77,channel=1):  # values 0-3 indictae the channel, anything else (eg -1) turns off all channels
        
        if   (channel==0): action = 0x04
        elif (channel==1): action = 0x05
        elif (channel==2): action = 0x06
        elif (channel==3): action = 0x07
        elif (channel==4): action = 0x08
        else : action = 0x00

        self.bus.write_byte_data(address,0x04,action)  #0x04 is the register for switching channels 

if __name__ == '__main__':
    
    bus=1       # 0 for rev1 boards etc.
    #address=0x70
    address=0x77
    plexer = multiplex(bus)
    plexer.channel(address,3)
    
    print("Now run i2cdetect")


