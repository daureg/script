#! /bin/sh

echo "Verifiez que vous avez nettoyé data et devel avant"
read anykey
cd $HOME
save_pkg
cp -r .bash* .fonts.conf .drirc .gvimrc .vim* .xinitrc .conf
tar caf pkg.tar.gz .pkg 
tar caf data.tar.gz data
tar caf devel.tar.gz devel
tar caf conf.tar.gz .conf
sudo tar caf etc.tar.gz /etc
echo "Dépécher vous de le copier quelque part"
