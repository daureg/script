#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys


# Quelques constantes
LEN_1_PART=12
LEN_2_PART=22
LEN_3_PART=13
LEN_4_PART=15

ARCH="| 2007.08 Don't Panic"
UBUNTU="| 7.04 Feisty Fawn"

SYSTEME="default"
KERNEL_NAME=""
VERSION=""
BOOT_KERNEL=""

TITLE="title\t\t"
TITLE_S=TITLE
RESTE=""
RESTE_S=""

def print_help():
    print "\n\nUsage : add_grub_entry [OPTIONS]"
    print "Imprime une nouvelle entrée pour le menu.lst de grub\n"
    print "\t -s\tle nom du systeme dans {win|ubuntu|arch}"
    print "\t -v\tla version du noyau (moins de "+str(LEN_3_PART-2)+" caractères)"
    print "\t -n\tle nom du noyau (moins de "+str(LEN_4_PART-2)+" caractères)"    
    print "\t -h\taffiche cette aide"
    sys.exit()

if (len(sys.argv) < 2):
    print "ERREUR : Il faut des arguments"
    print_help()
if (len(sys.argv) != 7 and not(sys.argv[1] == "-h" or sys.argv[1] == "--help")):
    print "ERREUR : Il faut six arguments"
    print_help()

for i in range(6) :
#L'aide
    if (sys.argv[i] == "-h" or sys.argv[i] == "--help"):
        print_help()
#Choix du système
    if (sys.argv[i] == "-s"):
        if (sys.argv[i+1] == "win" or 
            sys.argv[i+1] == "ubuntu" or
	    sys.argv[i+1] == "arch"):
            	SYSTEME=sys.argv[i+1]
        else:
            print "ERREUR : Mauvais système"
            print_help()
#Version du noyau
    if (sys.argv[i] == "-v"):
        if (len(sys.argv[i+1]) <= LEN_3_PART-2):
            VERSION=sys.argv[i+1]
        else:
            print "ERREUR : Version du noyau trop longue"
            print_help()
#Nom du noyau
    if (sys.argv[i] == "-n"):
        if (len(sys.argv[i+1]) <= LEN_4_PART-2):
            KERNEL_NAME=sys.argv[i+1]
        else:
            print "ERREUR : Nom de noyau trop longue"
            print_help()
            
# Voila, on a tous nos arguments
# Remplir BOOT_KERNEL
if (SYSTEME=="ubuntu"):
    BOOT_KERNEL="vmlinuz-"
BOOT_KERNEL=BOOT_KERNEL+VERSION+"-"+KERNEL_NAME

# Il faut maintenant remplir le titre

# partie 1 (systeme)
if (SYSTEME=="win"):
    TITLE=TITLE+"Windows"+(LEN_1_PART-7)*' '+"| XP Home"+(LEN_2_PART-8)*' '
    RESTE="root		(hd0,0))\nsavedefault\nmakeactive\nchainloader	+1"
if (SYSTEME=="ubuntu"):
    TITLE=TITLE+"Ubuntu"+(LEN_1_PART-6)*' '+"| 7.04 - Feisty Fawn"+(LEN_2_PART-len(UBUNTU))*' '
    RESTE="root		(hd0,8)\nkernel		/boot/"+BOOT_KERNEL+" root=/dev/sda9 ro quiet splash\nsavedefault\nboot"
    RESTE_S="root		(hd0,8)\nkernel		/boot/"+BOOT_KERNEL+" root=/dev/sda9 ro single\nboot"
if (SYSTEME=="arch"):
    TITLE=TITLE+"Archlinux"+(LEN_1_PART-9)*' '+"| 2007.08 - Don't Panic"+(LEN_2_PART-len(ARCH))*' '
    RESTE="root   (hd0,10)\nkernel /boot/vmlinuz26 root=/dev/sda11 ro\ninitrd /boot/kernel26.img"
    RESTE_S="root   (hd0,10)\nkernel /boot/vmlinuz26 root=/dev/sda11 ro\ninitrd /boot/kernel26-fallback.img"
TITLE=TITLE+"| "

# partie 3 (version)
TITLE=TITLE+VERSION+(LEN_3_PART-len(VERSION))*' '+"| "

# partie 4 (nom)
TITLE=TITLE+KERNEL_NAME+(LEN_4_PART-len(KERNEL_NAME))*' '

# dernieres finitions
TITLE_S=TITLE+"| S"


print TITLE+"\n"+RESTE+"\n\n"+TITLE_S+"\n"+RESTE_S
