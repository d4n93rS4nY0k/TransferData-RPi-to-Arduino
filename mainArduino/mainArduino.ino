#include <SPI.h>
#include <RF24.h>
#include "printf.h"

RF24 radio(9,10);

void setup(void){
  while(!Serial);
  Serial.begin(9600);
  
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xF0F0F0F0E1LL);

  const uint64_t pipe = 0xE8E8F0F0E1LL;
  radio.openReadingPipe(1, pipe);
  
  radio.enableDynamicPayloads();
  radio.powerUp();
  printf_begin(); 
  radio.printDetails();
  radio.startListening();
}

void loop(void){
  radio.startListening();
  char receivedMessage[32] = {0};
  if(radio.available()){
    radio.read(receivedMessage, sizeof(receivedMessage));
    Serial.println(receivedMessage);
    radio.stopListening();
  }
  delay(2000);
  }
