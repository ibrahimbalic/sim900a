import sys,msvcrt,time, serial # pip install pyserial

# serial port uzerinden 'com3' ardunio cihaza baglaniyoruz.
gsmkit = serial.Serial("COM3",9600,timeout=5)
# 4 saniye bekletiyoruz. 
time.sleep(4)
while True:
	# microsoft runtime ile Console I/O islemleri icin ekrana basilan tuslari takip ediyoruz.
	if msvcrt.kbhit():
		# consolda basilan tus varsa ve esc(keykodu 27) ise sistemden cikis yap diyoruz  
		if ord(msvcrt.getch()) == 27:
			# cikis
			sys.exit()
		# consolda basilan tus varsa ve tab(keykodu 9) ise input ile komut al
		if ord(msvcrt.getch()) == 9:
			gidecekkomut = input("Cihaza komut yolla:")
			# kullanicidan gelen komutu encode ederek ardunio'ya yolla 
			gsmkit.write(str(gidecekkomut.replace('\n','').replace('\r','')+"\r\n").encode('utf-8'))

	# ardunio uzerinden while ile veri okumak istiyoruz. gelen veriyi decode ediyoruz.
	# errors = kismi cihazdan UTF-8 disinda bir veri gelirse hata vermemesi icin.
	gelen = str(gsmkit.readline().decode('UTF-8', errors='replace'))
	# gelen veri iceriginde yeni satirlari siliyoruz
	gelen = gelen.replace('\r','').replace('\n','')
	# gelen veri bir karakterden fazla ise ekrana yansitiyoruz.
	if len(gelen) > 0:
		print(gelen)
		