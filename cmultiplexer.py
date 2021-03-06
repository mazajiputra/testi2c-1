#!/usr/bin/python

import smbus

class multiplex:
    
    def __init__(self, bus):
        self.bus = smbus.SMBus(bus)

    def channel(self, address,channel):  # values 0-7 indictae the channel, anything else (eg -1) turns off all channels
        #dipake 02,04,05,07
        #tidak dipake 00,01,03,04,06
        if   (channel==0): action = 0x01
        elif (channel==1): action = 0x02
        elif (channel==2): action = 0x04
        elif (channel==3): action = 0x08
        elif (channel==4): action = 0x10
        elif (channel==5): action = 0x20
        elif (channel==6): action = 0x40
        elif (channel==7): action = 0x80
        else : action = 0x00

        self.bus.write_byte_data(address,0x04,action)  #0x04 is the register for switching channels 

if __name__ == '__main__':
    
    bus=1       # 0 for rev1 boards etc.
    address=0x77
    
    plexer = multiplex(bus)
    pilih=2
    plexer.channel(address,pilih)
    print("channel yg dipilih ",pilih)
    print("Now run i2cdetect")