import time, serial # pip install pyserial

# serial port uzerinden 'com3' ardunio cihaza baglaniyoruz.
gsmkit = serial.Serial("COM3",9600,timeout=5)
# 4 saniye bekletiyoruz. 
time.sleep(4)
# hardware\arduino\avr\libraries\SoftwareSerial\src\SoftwareSerial.h
# define _SS_MAX_RX_BUFF 64 olarak geliyor, bu size'i 256 olarak duzenleyin
# boyutu buyuk smslerde veya tum smsleri okurken eksik okursunuz max rx buffer size yuzunden.
gsmkit.write("AT+CMGL=\"ALL\"\r\n".encode('utf-8'))
while True:
	# ardunio uzerinden while ile veri okumak istiyoruz. gelen veriyi decode ediyoruz.
	# errors = kismi cihazdan UTF-8 disinda bir veri gelirse hata vermemesi icin.
	gelen = str(gsmkit.readline().decode('UTF-8', errors='replace'))
	# gelen veri iceriginde yeni satirlari siliyoruz
	gelen = gelen.replace('\r','').replace('\n','')
	# gelen veri bir karakterden fazla ise ekrana yansitiyoruz.
	if len(gelen) > 0:
		print(gelen)
