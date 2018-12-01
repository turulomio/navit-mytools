#!/bin/bash
DATE=`date +%Y%m%d_%H%M%S`
GPS=`geopositioning`
FILE=/tmp/geopositioning_$DATE/audio.wav
FINALFILE=~/$DATE-$GPS.wav

mkdir -p /tmp/geopositioning_$DATE
aplay /usr/share/sounds/alsa/Front_Center.wav #Empieza
arecord  -d 5 -f cd  $FILE
sox $FILE $FINALFILE noiseprof /tmp/geopositioning_$DATE/audio.nfo
sox $FILE $FINALFILE noisered /tmp/geopositioning_$DATE/audio.nfo 0.075
aplay $FINALFILE
