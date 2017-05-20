#!/usr/bin/env bash

xclock -update 1 &
sleep 0.5;
window_id=$(xwininfo -name "xclock" | grep -oP "(?<=Window id: )0x[0-9a-f]+");
echo $window_id
sleep 0.5;
wmctrl -i -r $window_id -b add,above
wmctrl -i -r $window_id -e 0,1735,190,-1,-1;
