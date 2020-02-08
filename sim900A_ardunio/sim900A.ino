#include <SoftwareSerial.h>
/*
* bu kismi 7 ve 8 pin olarak ben 
* ayarladim siz ardunio uzerinde 
* hangi pinleri kullanacaksaniz ona gore duzenleyin.
*/
SoftwareSerial mySerial(7, 8); 
void setup()
{
  Serial.begin(9600);
  mySerial.begin(9600);
  Serial.println("Baslatiliyor...");
  delay(100);
  /* Cihazin hazir olmasini sagliyoruz.*/
  mySerial.println("AT");
  delay(100);
  /* 0 minimum functionality
   * 1 full functionality
   * 2 disable telefon iletim RF
   * 3 disable telefon alma RF
   * 4 disable telefon iletme ve alma RF
   * biz 1 ile full func kullanacagimizi bildiriyoruz.
   */ 
  mySerial.println("AT+CFUN=1");
  delay(100);
  /* 0 PDU MOD
   * 1 TEXT MOD
   * biz 1 ile text moda aliyoruz.
   */ 
  mySerial.println("AT+CMGF=1");
  updateSerial();
}

void loop()
{
  updateSerial();
}

void updateSerial()
{
  delay(500);
  /*  ardunio ile gsmkit arasinda while   
   *  dongusu olusturup, arduniodan   
   *  gsmkite veya gsmkitten ardunio   
   *  gelen veriyi takip ediyoruz. 
   */
  while (Serial.available()) 
  {
    mySerial.write(Serial.read());
      delay(1500);
  }
  while(mySerial.available()) 
  {
    Serial.write(mySerial.read());
  }
}
