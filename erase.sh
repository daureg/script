#! /bin/sh
DAY=`date +"%Y%m%d"`
TIME=`date +"%s"`
mkdir -p ~/.trash/$DAY/$TIME
mv -f "$@" ~/.trash/$DAY/$TIME
