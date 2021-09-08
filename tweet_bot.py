#!/bin/python3
import tweepy 
import random 
import sys
from bot import *

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(TOKEN, SECRET_TOKEN)

api = tweepy.API(auth)

hashtag = [ "geek", "live", "twitch", "programming", "jeux", "steam", "streaming", "chill" ]
str_hash = ""
i=0

while i <= HASHTAG -1:
    x = random.randint(0, len(hashtag)-1)
    str_hash = str_hash + " #"+hashtag[x]
    i+=1

heure = sys.argv[1]

tweet = "Je suis en live jusqu'à "+ heure +"h environ.\n\n https://twitch.tv/kawaegle/\n\n" + str_hash

print(tweet+"\n\n")
api.update_status(tweet)

print("[+] Tweet is send let's go live!!")
