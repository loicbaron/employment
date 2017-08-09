#!/bin/bash

# Path of the script
DIR=$(dirname "$0")

killall python
killall Python

# As deamon
$DIR/server.py >>$DIR/log/server-stdout-stderr.log 2>&1 &
