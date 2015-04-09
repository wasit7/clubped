// Demo using DHCP and DNS to perform a web client request.
// 2011-06-08 <jc@wippler.nl> http://opensource.org/licenses/mit-license.php

#include <EtherCard.h>

// ethernet interface mac address, must be unique on the LAN
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x30,0x31 };

byte Ethernet::buffer[700];
static uint32_t timer;

static byte hisip[] = { 192,168,1,35 };// remote webserver
//const char website[] PROGMEM = "10.200.30.55";
const char website[] PROGMEM = "google.com";

// called when the client request is complete
static void my_callback (byte status, word off, word len) {
  Serial.println(">>>");
  Ethernet::buffer[off+300] = 0;
  Serial.print((const char*) Ethernet::buffer + off);
  Serial.println("...");
}

void setup () {
  Serial.begin(9600);
  Serial.println(F("\n[webClient]"));

  if (ether.begin(sizeof Ethernet::buffer, mymac) == 0) 
    Serial.println(F("Failed to access Ethernet controller"));
  if (!ether.dhcpSetup())
    Serial.println(F("DHCP failed"));
    

  ether.printIp("IP:  ", ether.myip);
  ether.printIp("GW:  ", ether.gwip);  
  ether.printIp("DNS: ", ether.dnsip);  
  
  if (!ether.dnsLookup(website))
    Serial.println("DNS failed");
  ether.copyIp(ether.hisip, hisip);
  ether.printIp("Server: ", ether.hisip);
}

String str;
char chbuff[50];
void loop () {
  ether.packetLoop(ether.packetReceive());
  str=String(millis())+"/"+String(millis()%20);
  str.toCharArray(chbuff,20);
  if (millis() > timer) {
    timer = millis() + 1000;
    Serial.println();
    Serial.print("<<< REQ ");
    ether.browseUrl(PSTR("/log/"), (const char*)chbuff, website, my_callback);
    //ether.httpPost(PSTR("/log/"),website,PSTR("Accept: text/html"),(const char*)chbuff,my_callback);
  }
}
