#!/bin/bash
ARTIST=`osascript -e 'tell application "Spotify" to artist of current track as string'`
TRACK=`osascript -e 'tell application "Spotify" to name of current track as string'`
echo "$TRACK by $ARTIST genius lyrics"
curl -# -L https://genius.com/Anohni-why-did-you-separate-me-from-the-earth-lyrics | grep "<div class=\"lyrics\">"
