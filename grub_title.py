#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable-msg=W0312

import sys

# Quelques constantes
LEN_1_PART=10
LEN_2_PART=22
LEN_3_PART=10
LEN_4_PART=14

WIN="| XP Home"
ARCH="| 2007.11 Core Dump"
UBUNTU="| 7.10 Gutsy Gibbon"
FEDORA="| 8 Werewolf"

SYSTEME="default"
KERNEL_NAME=""
VERSION=""

TITLE="title\t\t"
TITLE_S=TITLE

def print_help():
    print "\n\nUsage : add_grub_entry [OPTIONS]"
    print "Imprime une nouvelle entrée pour le menu.lst de grub\n"
    print "\t -s\tle nom du systeme dans {win|ubuntu|arch|fedora}"
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
            sys.argv[i+1] == "fedora" or
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
            
# Il faut maintenant remplir le titre

# partie 1 (systeme)
if (SYSTEME=="win"):
    TITLE=TITLE+"Windows"+(LEN_1_PART-7)*' '+WIN+(LEN_2_PART-len(WIN))*' '
if (SYSTEME=="ubuntu"):
    TITLE=TITLE+"Ubuntu"+(LEN_1_PART-6)*' '+UBUNTU+(LEN_2_PART-len(UBUNTU))*' '
if (SYSTEME=="arch"):
    TITLE=TITLE+"Archlinux"+(LEN_1_PART-9)*' '+ARCH+(LEN_2_PART-len(ARCH))*' '
if (SYSTEME=="fedora"):
    TITLE=TITLE+"Fedora"+(LEN_1_PART-6)*' '+FEDORA+(LEN_2_PART-len(FEDORA))*' '
TITLE=TITLE+"| "

# partie 3 (version)
TITLE=TITLE+VERSION+(LEN_3_PART-len(VERSION))*' '+"| "

# partie 4 (nom)
TITLE=TITLE+KERNEL_NAME+(LEN_4_PART-len(KERNEL_NAME))*' '

# dernieres finitions
TITLE_S=TITLE+"| S"

print TITLE+"\n"+TITLE_S
