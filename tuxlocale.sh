#!/bin/bash

USERNAME="user"
PASSWORD="pass"
UPDATE_INTERVAL=300

python /opt/tuxlocale/tuxlocale --post $USERNAME $PASSWORD $UPDATE_INTERVAL >> /dev/null &
echo 'Tux Locale start [ok]'
