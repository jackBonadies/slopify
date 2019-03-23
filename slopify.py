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
def searchGoogle(artist, track):
  searchTerm = "genius lyrics"
  src=requests.get("https://www.google.com/search?q=" + artist + " " + track + " " + searchTerm).text
  soup = BeautifulSoup(src,'lxml')
  return soup
def getFirstLinkFromGoogle(soup):
  divs = soup.find_all('div')
  for div in divs:
    if(div.get('id')=="search"):
      searchResults = div
  links = searchResults.find_all('a')
  href = links[0].get('href')
  parts = href.split('&')
  part1 = parts[0]
  strippedURL = part1.replace('/url?q=','')
  return strippedURL
def getLyricsFromLink(url):
  src = requests.get(url).text
  soup = BeautifulSoup(src,'lxml')
  lyrics = soup.find('p')
  print(lyrics.text)
artist=getArtist()
title=getTrack()
src = searchGoogle(getArtist(),getTrack())
url = getFirstLinkFromGoogle(src)
#p = subprocess.Popen(['clear'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#p.communicate()
getLyricsFromLink(url)
