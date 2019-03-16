#!/bin/bash
ARTIST=`osascript -e 'tell application "Spotify" to artist of current track as string'`
TRACK=`osascript -e 'tell application "Spotify" to name of current track as string'`
echo "$TRACK by $ARTIST genius lyrics"
curl -# -L https://www.azlyrics.com/lyrics/anohni/4degrees.html -o temp.txt 
