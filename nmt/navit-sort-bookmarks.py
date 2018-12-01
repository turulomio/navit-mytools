#!/bin/bash
dat=`date +%Y%m%d_%H%M`
mv ~/.navit/bookmark.txt ~/.navit/bookmark.txt.$dat
sort -s -t$'"' -k 3 ~/.navit/bookmark.txt.$dat > ~/.navit/bookmark.txt

