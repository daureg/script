sudo pacman -Rnsdf libstdc++5 xinetd netkit-bsd-finger catalyst
sudo pacman -S libgl ati-dri xf86-video-ati testing/xorg-xserver
sudo sed -i -e '/catalyst/ s/^/#/' /etc/rc.conf
sudo sed -i -e '/radeon-hint/ s/^#//' /etc/rc.conf
sudo sed -i -e '/catalyst/ s/^/#/' /etc/X11/xorg.conf
sudo sed -i -e '/radeon-hint/ s/^#//' /etc/X11/xorg.conf
