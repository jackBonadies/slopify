#!/bin/bash
ARTIST=`osascript -e 'tell application "Spotify" to artist of current track as string'`
TRACK=`osascript -e 'tell application "Spotify" to name of current track as string'`
echo "$TRACK by $ARTIST lyrics"
curl -# -L https://www.lyrics.com/lyric/32840200/$ARTIST/$TRACK -o temp.txt 
echo "--------------------------"
./regexPy.py
