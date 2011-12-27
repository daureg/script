#! /usr/bin/env python
# vim: fileencoding=utf-8 :
# pylint: disable-msg=W0312
"""Compare the output of lsmod with the module directory of the running kernel
to find module which were built but which aren't used."""
import sys, os, tempfile

def get_info(lsmod, ko_built):
    """Fill the 'lsmod' list with the output of lsmod and the 'ko_built'
    with the built kernel module found in the module directory of the
    running kernel."""
    lsmod_out = tempfile.NamedTemporaryFile()
    os.system("lsmod >" + lsmod_out.name)
    lsmod_out.flush()
    for line in lsmod_out:
        lsmod.append(line.split()[0])

    build_out = tempfile.NamedTemporaryFile()
    os.system("ls -R /lib/modules/`uname -r`/kernel | \
              grep \"ko$\">" + build_out.name)
    for line in build_out:
        ko_built.append(line[:-4])

if __name__ == "__main__":
    NEEDED = []
    BUILD = []
    UNWANTED = []
    get_info(NEEDED, BUILD)
    #UNWANTED = [i for i in BUILD if i not in NEEDED]
    UNDERSCORE_BUILD = [i.replace('-','_') for i in BUILD]
    for i in range(len(UNDERSCORE_BUILD)):
        if UNDERSCORE_BUILD[i] not in NEEDED:
            UNWANTED.append(BUILD[i])
            print(os.popen("find \
                          /lib/modules/`uname -r`/kernel/* -name "\
                           + BUILD[i] + ".ko" + "|cut -d / -f6-").read().strip())

    if len(UNWANTED) > len(NEEDED):
        print("ERROR : non coherent result !")
        print("%d > %d " % \
              (len(UNWANTED), len(NEEDED)))
    else:
        print("OK : Coherent result !")
        print("%d < %d " % \
              (len(UNWANTED), len(NEEDED)))

    sys.exit()
