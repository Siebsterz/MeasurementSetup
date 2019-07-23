import adafruit_ina219
from ina219 import INA219

ina = INA219(shunt_ohms = 0.1, max_expected_amps = 0.5, address=0x40)

#currentSensor = adafruit_ina219.INA219()

ina.configure(voltage_range = ina.RANGE_16V, gain = ina.GAIN_AUTO, bus_adc = ina.ADC_128SAMP, shunt_adc = ina.ADC_128SAMP)

V = ina.voltage()
I = ina.current()
P = ina.power()
