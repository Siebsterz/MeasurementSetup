# Import the MCP4725 module.
import Adafruit_MCP4725

# Create a DAC instance.
dac = Adafruit_MCP4725.MCP4725(address=0x60)

# Note you can change the I2C address from its default (0x62), and/or the I2C
# bus by passing in these optional parameters:
#dac = Adafruit_MCP4725.MCP4725(address=0x49, busnum=1)


#desired voltage = (reference voltage/ resolution)  * digital value
#digital value = desired voltage * (resolution/reference voltage)
reference_voltage = 5
resolution = 4096	#12bit DAC

def DACVoltage(desired_voltage):
    digital_value = float(desired_voltage) * (resolution/reference_voltage)
    print("desired voltage = " + str(desired_voltage))
    print("digital voltage = " + str(digital_value))
    print("digital voltage = " + str(round(digital_value)))
    dac.set_voltage(round(digital_value))



