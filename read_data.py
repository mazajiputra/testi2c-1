import time
from struct import unpack
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, \
    I2cDevice, SensirionI2cCommand, CrcCalculator
from sensirion_i2c_sht.sht3x import Sht3xTemperature, Sht3xHumidity


class Shtc3I2cCmdMeasure(SensirionI2cCommand):
    def __init__(self):
        super(Shtc3I2cCmdMeasure, self).__init__(
            command=0x7866,
            tx_data=[],
            rx_length=6,
            read_delay=0.02,
            timeout=0,
            crc=CrcCalculator(8, 0x31, 0xFF),
        )

    def interpret_response(self, data):
        checked_data = SensirionI2cCommand.interpret_response(self, data)
        temperature_ticks, humidity_ticks = unpack(">2H", checked_data)
        return Sht3xTemperature(temperature_ticks), Sht3xHumidity(humidity_ticks)

time.sleep(1) #wait here to avoid 121 IO Error

with LinuxI2cTransceiver('/dev/i2c-1') as transceiver:
    device = I2cDevice(I2cConnection(transceiver), 0x70)
    temperature, humidity = device.execute(Shtc3I2cCmdMeasure())
    print("Temperature: {}, Humidity: {}".format(temperature, humidity))
