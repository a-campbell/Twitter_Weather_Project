from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json
access_token = "20283926-IIH9J0azYI93f3VZ3zHbiOFqABXTQ3aivMA3Mjw1c"
access_token_secret = "9590z227cf1s9qPKDRfkGSahfOAO9ge8rj6NTyIi97WmN"
consumer_key = "Hi7w67EqoiyOSjPbCFeq1mmkl"
consumer_secret = "Rac1HDteRdGD6Hblbn2mg2y9al5IWqZGfVTY8chWi8UliDSJOo"

weatherwords = ["weather", "rain"]

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
        stream.filter(track=weatherwords)
        
    except KeyboardInterrupt:
        #User pressed ctrl+c -- get ready to exit the program
        pass

    #Close the output file 
    fhOut.close()


