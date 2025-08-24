#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>
char Incoming_value = 0;
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN); 
Servo myServo; 

 
void setup() 
{
  Serial.begin(9600);  
  SPI.begin();      
  mfrc522.PCD_Init();   
  myServo.attach(3); 
  myServo.write(0); 
  Serial.println("Put your card to the reader...");
  Serial.println();

}
void loop() 
{
  if(Serial.available() > 0)  
  {
    Incoming_value = Serial.read();            
    Serial.print("\n");        
    if(Incoming_value == '1'){   
      Serial.println("Guest Entered.");          
      myServo.write(90);
      delay(3000); 
      myServo.write(0);
    }
    else if(Incoming_value == '0'){       
      myServo.write(0);
      delay(1000);
    }   
  }              
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  Serial.println();
  Serial.print("Message : ");
  content.toUpperCase();

  if (content.substring(1) == "5A A7 5B 19" || content.substring(1)== "04 2C 0F 0A 09 6C 80")
  {
    Serial.println("Authorized access.");
     if (content.substring(1) == "5A A7 5B 19")
     {
      Serial.println("\nA Entered.");
     }
     
     if (content.substring(1) == "04 2C 0F 0A 09 6C 80")
     {
      Serial.println("\nB Entered.");
     }
    
    
    Serial.println();
    myServo.write(90);
    delay(3000);
    myServo.write(0);
  }
 
 else{
    Serial.println(" Access denied! Proceed with bluetooth entry for guests.");
  }
}
