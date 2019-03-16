#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import os
import subprocess

def getArtist():
	script = 'tell application "Spotify" to artist of current track as string' 
	p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	stdout, stderr = p.communicate(script)
	return stdout
def getTrack():
        script = 'tell application "Spotify" to name of current track as string'
        p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = p.communicate(script)
        return stdout
artist=getArtist()
title=getTrack()
#print(artist + " " + title)
title = title.replace(' ','-')
title = title.replace('\n','')
title = title.replace('?','')
artist = artist.replace('\n','')
url=artist+"-"+title+"-lyrics"
#print(url)
source=requests.get('https://genius.com/' + url).text
soup=BeautifulSoup(source,'lxml')
lyrics=soup.find('p')
print(artist + ": " + title + " lyrics")
print("-------------------------------------------------------------------")
print(lyrics.text)
