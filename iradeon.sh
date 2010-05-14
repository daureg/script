sudo pacman -Rnsdf libstdc++5 xinetd netkit-bsd-finger catalyst-utils catalyst
sudo pacman -S libgl
sudo sed -i -e '/catalyst/ s/^/#/' /etc/rc.conf
sudo sed -i -e '/radeonhd/ s/^#//' /etc/rc.conf
sudo sed -i -e '/catalyst/ s/^/#/' /etc/X11/xorg.conf
sudo sed -i -e '/radeonhd-hint/ s/^#//' /etc/X11/xorg.conf
