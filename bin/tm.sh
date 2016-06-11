#!/bin/bash

SESSIONNAME="display"
tmux has-session -t $SESSIONNAME &> /dev/null

if [ $? != 0 ] 
 then
    tmux new-session -s $SESSIONNAME -n main -d
    tmux send-keys -t $SESSIONNAME "/usr/bin/sudo /home/pi/bin/lcd.sh" C-m 
fi
