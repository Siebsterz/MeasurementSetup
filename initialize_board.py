def initializeBoard():
    try:
        from pyfirmata import Arduino, util
    except:
        try:
            from pip import main as pipmain
        except ImportError:
            from pip._internal import main as pipmain
        pipmain(['install', 'pyfirmata'])

        from pyfirmata import Arduino, util

    print("Correctly initialized")

    import time
    import math
    import warnings
    import serial
    import serial.tools.list_ports

    print("Connecting to board...")

    ports = list(serial.tools.list_ports.comports())
    print('Ports' + str(ports))
    allowedPorts = list()
    for p in ports:
        if 'ser' or 'Ser' or 'Arduino' in p.description:
            allowedPorts.append(p)
            if not allowedPorts:
                raise IOError("No board found")
            if len(allowedPorts) > 1:
                warnings.warn('Multiple boards connected - using the first available')

    print('Serial ports:' + str(allowedPorts))

    port = 'COM' + str(allowedPorts[0].description.split('COM')[1][0])


    board = Arduino(port)

    print("Connected!")

    iterator = util.Iterator(board)
    iterator.start()
    time.sleep(0.1)

    return board
