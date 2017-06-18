# Twitter-Mood-Lamp
A lamp reflecting the mood of Twitter.

This is a Twitter based mood lamp based on an Arduino and an Orange Pi Zero. The fetching of the Tweets and sentiment analysis happens on the Orange Pi Zero, which communicates the color to be displayed to the Arduino. The Arduino uses its PWM pins to show the right color on an RGB LED. This is because of the fact that the Orange Pi Zero has only one PWM pin.

Hardware needed:
  1. Any Single Board Computer. This was done on an Orange Pi Zero, but as no GPIOs are used, any SBC should do.
  2. Any Arduino. I used an Arduino Nano for this job. But pretty much anything works.

Libraries used: 
  1. pySerial : For communication between the Arduino and the Orange Pi.
  2. Tweepy : For fetching the tweets from Twitter.
  3. TextBlob : For text processing.
  
To run:
  1. Create a new application on dev.twitter.com and generate the Oauth keys. Change the .py file in this project and enter the keys.
  2. Upload the .ino file to the Arduino of your choice and the .py to any single board computer and run it. 
  3. The .py file assumes that the connected Arduino is at /dev/ttyUSB0. Change it if required. Also, you can change the PWM pins as per the Arduino board used. Connect the red, green and blue leads of an RGB LED to the three pins mentioned in the .ino file and the fourth lead to either 5V or GND, depending on whether it's common cathode or common anode. The .ino file assumes that the LED used is a common-anode RGB LED. The subtraction steps at the bottom have to be commented our for a common-cathode LED.
