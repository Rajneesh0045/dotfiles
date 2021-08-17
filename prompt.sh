#!/bin/sh
# A dmenu binary prompt script.
# Gives a dmenu prompt labeled with $1 to perform command $2
# Example: 
# `./prompt "Do you want to shutdown?" "shutdown -h now"`

[ $(echo "No\nYes" | rofi -dmenu -i -p "$1") = "Yes" ] && $2
