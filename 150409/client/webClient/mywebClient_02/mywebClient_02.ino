// Demo using DHCP and DNS to perform a web client request.
// 2011-06-08 <jc@wippler.nl> http://opensource.org/licenses/mit-license.php

#include <EtherCard.h>

// ethernet interface mac address, must be unique on the LAN
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x30,0x31 };

byte Ethernet::buffer[700];
static uint32_t timer;

static byte hisip[] = { 192,168,1,33 };// remote webserver
//const char website[] PROGMEM = "10.200.30.55";
const char website[] PROGMEM = "google.com";

// called when the client request is complete
static void my_callback (byte status, word off, word len) {
  Ethernet::buffer[off+300] = 0;
}

void setup () {
  ether.begin(sizeof Ethernet::buffer, mymac); 
  ether.dhcpSetup();
  ether.copyIp(ether.hisip, hisip);
}

String str;
char chbuff[50];
void loop () {
  ether.packetLoop(ether.packetReceive());
  str=String(millis());
  str.toCharArray(chbuff,10);
  if (millis() > timer) {
    timer = millis() + 100;
    ether.browseUrl(PSTR("/log/"), (const char*)chbuff, website, my_callback);
  }
}
