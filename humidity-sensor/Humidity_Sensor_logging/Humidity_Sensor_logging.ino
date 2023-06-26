#include "Adafruit_Si7021.h"
#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const int chipSelect = 4;
int indexx = 0;

Adafruit_Si7021 sensor = Adafruit_Si7021();

//display dimensions
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Serial.begin(115200);

  // wait for serial port to open
//  while (!Serial) {
//    delay(10);
//  }

  Serial.println("Si7021 test!");
  
  if (!sensor.begin()) {
    Serial.println("Did not find Si7021 sensor!");
  }

  Serial.print("Found model ");
  switch(sensor.getModel()) {
    case SI_Engineering_Samples:
      Serial.print("SI engineering samples"); break;
    case SI_7013:
      Serial.print("Si7013"); break;
    case SI_7020:
      Serial.print("Si7020"); break;
    case SI_7021:
      Serial.print("Si7021"); break;
    case SI_UNKNOWN:
    default:
      Serial.print("Unknown");
  }
  Serial.print(" Rev(");
  Serial.print(sensor.getRevision());
  Serial.print(")");
  Serial.print(" Serial #"); Serial.print(sensor.sernum_a, HEX); Serial.println(sensor.sernum_b, HEX);

// see if the SD card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    digitalWrite(13, HIGH);
//    while (1);
  }
  Serial.println("card initialized.");

//  initialize the display
//
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); // initialize with the I2C address 0x3C (for the 128x32)
  display.clearDisplay(); // Clear the display
}

void loop() {


// make a string for assembling the data to log:
  String dataString = "";
  String displayString1 = "";
  String displayString2 = "";
  indexx++;

//  write sensor data to dataString
  dataString += String(indexx);
  dataString += ",";
  dataString += String(sensor.readHumidity());
  dataString += ",";
  dataString += String(sensor.readTemperature() * 9/5 +32, 2);
//not readable pin
//  dataString += ",";
//  dataString += ((float)analogRead("VBAT"))/1024*3.3;

//  write sensor data to display string
  displayString1 += "H " + String(sensor.readHumidity()) + " %";
  displayString2 += "T " + String(sensor.readTemperature() * 9/5 +32, 2) + " F";
  

  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  File dataFile = SD.open("datalog.txt", FILE_WRITE);
  dataFile.close();
  dataFile = SD.open("datalog.txt", FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
    digitalWrite(8, HIGH);
    digitalWrite(13, LOW);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
    digitalWrite(8, LOW);
    digitalWrite(13, HIGH);
  }

//  draw to the display
display.clearDisplay(); // Clear the display
display.setTextSize(2); //Set our text size, size 1 correlates to 8pt font
display.setTextColor(WHITE); //We're using a Monochrome OLED so color is irrelevant, pixels are binary.
display.setCursor(0,0); //Start position for the font to appear
display.println(displayString1); //Will display text on new line
display.println(displayString2); //Will display text on new line
display.display();

  //  wait 1 second
  delay(1000);
}
