sudo pacman -S catalyst
sudo sed -i -e '/catalyst/ s/^#//' /etc/rc.conf
sudo sed -i -e '/radeonhd/ s/^/#/' /etc/rc.conf
sudo sed -i -e '/catalyst/ s/^#//' /etc/X11/xorg.conf
sudo sed -i -e '/radeonhd-hint/ s/^/#/' /etc/X11/xorg.conf
echo "Redemarrer sur le noyau officiel"
