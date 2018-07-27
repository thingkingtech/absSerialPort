import sys
import glob
import serial

from bottle import route, run, request

opt_1 = b'1'
opt_2 = b'2'
opt_3 = b'3'
opt_4 = b'4'
opt_5 = b'5'

BAUD_RATE = 9600
TEENSY_COM_1 = None
TEENSY_COM_2 = None
TEENSYPORTS = [None,None]
ser = [None,None]

def serial_ports():

    ports = ['COM%s' % (i + 1) for i in range(256)]
    
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def serial_init():
	Teensy_ports = serial_ports()
	count = 0
	for port in Teensy_ports:
		TEENSYPORTS[count] = port 
		print TEENSYPORTS[count]
		try:	
			global ser
			ser[count] = serial.Serial(TEENSYPORTS[count],BAUD_RATE,timeout=1)
		except Exception:
			raise IOError('could not connect to Teensy')
		count+=1

@route('/', method='get')
def index():
    serial_init()
    option = request.query['option']
    for i in range(2):
	if(ser[i] != None):			

	    if request.query['option'] =='1':
                ser[i].write(opt_1)	
            if request.query['option'] =='2':
	        ser[i].write(opt_2)	
            if request.query['option'] =='3':
	        ser[i].write(opt_3)
            if request.query['option'] =='4':
	        ser[i].write(opt_4)    	
            if request.query['option'] =='5':
	        ser[i].write(opt_5)
	    ser[i].close()
	    ser[i] = None
    return 'thank you very much'
	
run(host='localhost', port=8080, debug=True)