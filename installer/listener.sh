#!/bin/bash
cd /var/deploybot/watchlist
while SCRIPT=$(inotifywait -e create $DIR --format %f .)
do
    # Script is in the format timestamp=hostname.domain
    SERVER="${SCRIPT#*=}"
    (eval "ssh -o BatchMode=yes -o StrictHostKeyChecking=no $SERVER 'bash -s' < $SCRIPT"; rm "$SCRIPT") &
done