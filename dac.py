import board
import busio
import adafruit_mcp4725

i2c = busio.I2C(board.SCL, board.SDA)

dac = adafruit_mcp4725.MCP4725(i2c)

def setVoltage(voltage):
    dac.normalized_value(voltage)

