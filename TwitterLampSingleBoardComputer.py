import tweepy
from textblob import TextBlob
import serial
import time
import math

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 115200
ser.open()

consumer_key = <your-consumer-key>
consumer_secret = <your-consumer-secret>
access_token = <your-access-token>
access_token_secret = <your-access-token-secret>
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
while True :
	sentiment = 0.0
	red = 0.0
	blue = 0.0
	green = 0.0
	posThreshold = 0.3
	negThreshold = -0.3
	search_results = api.search(q="India", count=100)
	for tweet in search_results :
    		textToAnalyze= TextBlob(tweet.text)
    		sentiment = sentiment + textToAnalyze.sentiment.polarity

	avgSentiment = sentiment/100
	if avgSentiment < posThreshold and avgSentiment > negThreshold :
    		red = posThreshold - avgSentiment
    		green = avgSentiment - negThreshold
    		blue = (red + green) / 2
	elif avgSentiment > posThreshold :
    		green = 1.0
    		red = 0
    		blue = 0
	elif avgSentiment < negThreshold :
    		red = 1.0
    		blue = 0
   		green = 0

	red = red * 1000 - 1
	blue = blue * 1000 - 1
	green = green * 1000 - 1
        total = red + blue + green
	redColor = int((red/total) * 255)
	blueColor = int((blue/total) * 255)
	greenColor = int((green/total) * 255)
	RGBString = str(redColor) + "-" + str(greenColor) + "-" + str(blueColor)
        print avgSentiment
	print RGBString
	ser.write(RGBString)

	time.sleep(10)
