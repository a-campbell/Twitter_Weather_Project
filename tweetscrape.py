from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

allcords = [-0.530, 51.322, 0.231, 51.707, -74.255, 40.2557, -73.689, 40.9176,-87.968, 41.625, -87.397, 42.074,-118.9448, 32.8007, -117.646, 34.823,-122.472, 47.4224, -122.176, 47.7451,-71.898, 42.156, -71.020, 42.736, -80.87, 25.137, -80.118, 25.979]

class StdOutListener(StreamListener):

    #This function gets called every time a new tweet is received on the stream
    def on_data(self, data):

        #Convert the data to a json object (shouldn't do this in production; might slow down and miss tweets)
        j=json.loads(data)

        #If the tweet is not a retweet, not a response, and has a geolocation...
        if j["coordinates"] != None:      
#(j["in_reply_to_status_id"] == 'null') & (
        	#write the tweet to our output file      
	        fhOut.write("%s\n" % [j["id"],j["created_at"], j["coordinates"], j["lang"], j["text"]])
        
    def on_error(self, status):
        print("ERROR")
        print(status)

if __name__ == '__main__':
    try:
        #Create a file to store output. "a" means append (add on to previous file)
        fhOut = open("tweetoutput8.txt","a")

        #Create the listener
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        #Connect to the Twitter stream
        stream = Stream(auth, l)

        #filter our stream to the cities of interest
        stream.filter(locations=allcords)
        
    except KeyboardInterrupt:
        #User pressed ctrl+c -- get ready to exit the program
        pass

    #Close the output file 
    fhOut.close()


