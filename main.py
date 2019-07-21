import initialize_board
#import adafruit_mcp4725
import time
#import setVoltage
board = initialize_board.initializeBoard()

#setVoltage.voltage()

led = board.get_pin('d:10:p')
turnOff = board.get_pin('d:3:i')

led.write(100)

#dac = adafruit_mcp4725.MCP4725

#dac.normalized_value(1)




"""
def fadeInLED():
    for i in range(10):
        if turnOff.read() == 1:
            break
        led.write(i/10)
        time.sleep(0.05)

def fadeOutLED():
    for i in reversed(range(10)):
        if turnOff.read() == 1:
            break
        led.write(i/10)
        time.sleep(0.05)


while True:
        fadeInLED()
        if turnOff.read() == 1:
            break
        fadeOutLED()
        if turnOff.read() == 1:
            break

if turnOff.read() == 1:
    led.write(0)
"""

#board.exit()


