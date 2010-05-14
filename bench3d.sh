cat /proc/pci | grep VGA || lspci | grep VGA | colrm 1 4 ; cat /proc/cpuinfo | \
egrep "model name|MHz" ; xdpyinfo | egrep "version:|dimensions|depth of" ; glxinfo | \
egrep -A2 "direct rendering|OpenGL vendor" ; glxgears & sleep 25 ; killall glxgears