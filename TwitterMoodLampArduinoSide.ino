int redLED = 3;
int greenLED = 10;
int blueLED = 11;

void setup() {
  // initialize both serial ports:
  Serial.begin(115200);
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
 // read from port 0, send to port 1:
  if (Serial.available()) {
     String colorString = Serial.readString();
     int redString, blueString, greenString;
      for (int i = 0; i < colorString.length(); i++) {
        if (colorString.substring(i, i+1) == "-") {
          redString = colorString.substring(0, i).toInt();
          greenString = colorString.substring(i+1).toInt();
          for (int j = i+1; j < colorString.length(); j++) {
             if (colorString.substring(j, j+1) == "-") {
                blueString = colorString.substring(j+1).toInt();
                break;
        }
      }
          break;
        }
      }

      analogWrite(redLED, 255-redString);
      analogWrite(greenLED, 255-greenString);
      analogWrite(blueLED, 255-blueString);
      Serial.println(redString);
      Serial.println(greenString);
      Serial.println(blueString);
  }
}
