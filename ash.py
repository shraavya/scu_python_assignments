""" Streaming twitter API example """
from __future__ import print_function
import sys
import tweepy
from ConfigParser import ConfigParser


class TwitterListener(tweepy.StreamListener):
    count = 0
    twitterList = []
    twitterWord = []
    validWords = []
    dictWords = {}
    sortedDict = {}
    """ Twitter stream listener. """
    def on_status(self, tweet):
    	if '2026' in tweet.text:
            	print(tweet.text)
		return False
        else:
		return True

    #Function defination to eliminate stop words
    def isValidWord(self,wordTempArray):
        if len(wordTempArray) == 1:
           return False
        elif wordTempArray in ('donald','hillary','clinton','us','usa','rt','the','there','was','is', 'in','not','so','2016','on', 'to','voters','trump,','mr.','he\'s',
        'america','we','get','be','washington','if','were','pence','vote','november','are','has','she','he','am','for','or','his','her','of','cnn','fox','year',
        'poll','why','also','have','what','ok','did','election','president','it','by','and','&','with','live','with','gov','government','more','debate','presidency',
        'you','this','that','trump','just','they','as','my','can','all','clinton\'s','should','&amp', 'at','from','off','who','&amp;','trump:', 'via', 'would','new',
        'one','even','october','american','--','trump.','trump\'s','says','like','i\'m','true','campaign','voting','it\'s', 'that\'s','go','tells','people','know','see','don\'t','still'):
            return False
        elif wordTempArray in TwitterListener.stop:
            return False
        elif wordTempArray[0] == '@':
            return False
        elif wordTempArray[:4] == 'http':
            return False

        else:
            return True
     # Functiont to puplulate the dictionary with key(words in tweets), value(count)   
    def populateDict(self,item):
        if item in TwitterListener.dictWords.keys():
            TwitterListener.dictWords[item] = TwitterListener.dictWords[item] +1
            return TwitterListener.dictWords
        else:
            TwitterListener.dictWords[item] = 1
            return TwitterListener.dictWords
                            
    
    def on_error(self, msg):
        print('Error: %s', msg)

    def on_timeout(self):
        print('timeout : wait for next poll')
        sleep(10)
   
    

def get_config():
    """ Get the configuration """
    conf = ConfigParser()
    conf.read('sample.cfg')
    return conf

def get_stream():
    config = get_config()
    auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'),
                               config.get('twitter', 'consumer_secret'))

    auth.set_access_token(config.get('twitter', 'access_token'),
                          config.get('twitter', 'access_token_secret'))

    listener = TwitterListener()
    stream = tweepy.Stream(auth=auth, listener=listener)
    return stream

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: %s <word_1> <word_2>" % (sys.argv[0]))
    else:
        word = sys.argv[1]
        stream = get_stream()
        print("Listening to '%s' and '%s' ..." %('#' + word, word))
        stream.filter(track=['#' + word, word])
    
        
"""
I have run the above python pogram for both clinton and trump and ran the program for 1000 tweets
python tweetering.py clinton
python tweetering.py trump
Instead of creating a dictionary to compute frequencies of the words as above, we can use the python module collections to compute frequencies automatically.  
Sentimental Analysis value ( +1 - for a positive word, -1 for a negative word)

Top 10 words for clinton
[(u'wikileaks', 114), (u'emails', 85), (u'goldman', 76), (u'sachs', 60), (u'bill', 59), (u'released', 54), (u'today', 45), (u'th\u2026', 44), (u'journalism', 43),
(u'transcripts.', 43)]
Score
wikileaks  = -1 , On going wikileaks issues
emails = -1 , On going emails controversy
goldman sachs = -1 , released wikileaks goldmansachs speeches
bill = -1 , Assuming Sexual assault cases aganist Bill Clinton's
released = -1 , pertaining to released wikileaks emails/speeches
today = 0 , very nuetral word
juonralism = 0 , very nuetral word
transcripts = -1 , transcripts released by wikileaks

Score = -6 

Top 10 words for trump'
[(u'women', 55), (u'#trump', 39), (u'media', 39), (u'think', 28), (u'#maga', 27), (u'supporters', 26), (u'never', 24), (u'every', 23), (u'rally', 21), (u'gop', 20)]

Score
women = -1
#trump = 0
media = 0
think = 0
supporters = 1
never = 
every =
rally =
gop = -1

"""
