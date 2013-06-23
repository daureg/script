#! /usr/bin/python2
# vim: fileencoding=utf-8 :
#pylint: disable-msg=W0312
"""Write a PKGBUILD from answer from interactive question"""
import sys, os, types
from subprocess import check_output as co


def maintainer(current_file):
    """Write the maintainer name found in makepkf.conf in file's start"""
    current_file.seek(0, 0)
    maint = co('grep PACKAGER /etc/makepkg.conf', shell=True).split('"')[1]
    current_file.write("# Contributor: "+maint+"\n\n")


def write_value(name, value, current_file, quote=True, array=True):
    """Write the name plus the value or the list of the value in current_file
    If quote is set to true (default), it adds quote around the element"""
    to_write = ""
    if value == "":
        to_write += "#"

    to_write += name+"="
    if array:
        if isinstance(value, list):
            to_write += "("+" ".join(map(lambda x: "'"+x+"'", value))+")"

        else:
            if quote:
                to_write += "(\'"+value+"\')"
            else:
                to_write += "("+value+")"

    else:
        if quote:
            to_write += "\""+value+"\""
        else:
            to_write += value

    to_write += "\n"
    current_file.write(to_write)


def error(current_file):
    """Error message, close the current_file and exit"""
    print "You made a mistake."
    print "Try 'man PKGBUILD' or go to"
    print " http://wiki.archlinux.org/index.php/Arch_Packaging_Standards"
    print " for more help"
    current_file.close()
    sys.exit()


def ask_value(name, default=None, could_be_empty=False, choice=None,
              full_string=False):
    """Ask for name's value. You could provide a default value and a list of
    choice (only for help). Return -1 in case of error."""
    if name == "pkgdesc":
        full_string = True

    question = "Fill "+name
    if could_be_empty:
        default = ""

    if default is not None:
        question += "\n("+default+")"

    if choice is not None:
        if isinstance(choice, str):
            question += "\n["+choice+"] --> "

        else:
            question += "\n[{}] --> ".format(" ".join(choice))

    else:
        question += " --> "

    result = raw_input(question)
    return control_value(result, default, full_string)


def control_value(result, default, full_string):
    """Control the value of the anwser with the optional argument."""
    if len(result) > 0:
        if result.find(" ") == -1 or full_string:
            return result
        else:
            result = result.split()
            result = [j.strip("\"\'") for j in result]
            return result
    else:
        if default is not None:
            return default
        else:
            return -1


def get_update_method(pkgname):
    """Find the method for fetching the source code of the package."""
    if pkgname.find("cvs") != -1:
        return "cvs"
    if pkgname.find("svn") != -1:
        return "svn"
    if pkgname.find("git") != -1:
        return "git"
    if pkgname.find("bzr") != -1:
        return "bzr"
    if pkgname.find("hg") != -1:
        return "hg"
    if pkgname.find("darcs") != -1:
        return "darcs"
    else:
        return "release"


def mk_vim_end(current_file):
    """Write vim option at the end of the current_file."""
    current_file.write("# vim: set ft=sh ts=2 sw=2 et:\n")


def mk_pkgver(current_file, build_method):
    if build_method == "release":
        return
    first = "\npkgver() {\n"
    if build_method == "svn":
        first += "\tcd $_svnmod; svnversion | tr -d [A-z]"
    if build_method == "git":
        first += "\tcd $_gitname; echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)"
    if build_method == "hg":
        first += "\tcd $_hgrepo; echo $(hg identify -n).$(hg identify -i)"
    if build_method == "bzr":
        first += "\tcd $_hgrepo; bzr revno"
    if len(first) > 15:
        current_file.write(first+"\n}")
    else:
        current_file.write("\tdate +%Y%m%d\n}")


def mk_build(current_file, build_method):
    """Fill the build method of the package."""
    first = "\nbuild() {\n\tcd ${srcdir}\n"
    if build_method == "svn":
        svntrunk = ask_value("_svntrunk")
        svnmod = ask_value("_svnmod")
        write_value("_svntrunk", svntrunk, current_file, False, False)
        write_value("_svnmod", svnmod, current_file, False, False)
        write_value('source', "{}::{}".format(svnmod, svntrunk), current_file)
        first += "\tmsg \"Connecting to $_svnmod SVN server...\"\n"
        first += "\tif [ -d $_svnmod/.svn ]; then \n"
        first += "\t\t(cd $_svnmod && svn up -r $pkgver) \n"
        first += "\telse \n"
        first += "\t\tsvn co $_svntrunk --config-dir ./ -r $pkgver $_svnmod \n"
        first += "\tfi \n"
        first += "\tmsg \"SVN checkout done or server timeout\"\n"
        first += "\tcd $_svnmod\n"
        sdir = "$_svnmod"

    if build_method == "bzr":
        bzrtrunk = ask_value("_bzrtrunk")
        bzrmod = ask_value("_bzrmod")
        write_value("_bzrtrunk", bzrtrunk, current_file, False, False)
        write_value("_bzrmod", bzrmod, current_file, False, False)
        write_value('source', "{}::{}".format(bzrmod, bzrtrunk), current_file)
        first += "\tmsg \"Connecting to $_bzrmod BZR server...\"\n"
        first += "\tif [ -d $_bzrmod/.bzr ]; then \n"
        first += "\t\t(cd $_bzrmod && bzr up) \n"
        first += "\telse \n"
        first += "\t\tbzr co $_bzrtrunk $_bzrmod \n"
        first += "\tfi \n"
        first += "\tmsg \"BZR checkout done or server timeout\"\n"
        first += "\tcd $_bzrmod\n"
        sdir = "$_bzrmod"

    if build_method == "cvs":
        write_value("_cvsroot", ask_value("_cvsroot"), current_file, False, False)
        write_value("_cvsmod", ask_value("_cvsmod"), current_file, False, False)
        second = "\nprepare() {\n\tcd ${srcdir}\n"
        second += "\tmsg \"Connecting to $_cvsmod CVS server...\"\n"
        second += "\tif [ -d $_cvsmod/CVS ]; then\n"
        second += "\t\t(cd $_cvsmod && cvs -z3 update -d) \n"
        second += "\telse \n"
        second += "\t\t(cvs -z3 -d $_cvsroot co -D $pkgver -f $_cvsmod)\n"
        second += "\tfi \n"
        second += "\tmsg \"CVS checkout done or server timeout\"\n"
        current_file.write(second+'}')
        first += "\tcd $_cvsmod\n"
        sdir = "$_cvsmod"

    if build_method == "git":
        gitroot = ask_value("_gitroot")
        gitname = ask_value("_gitname")
        write_value("_gitroot", gitroot, current_file, False, False)
        write_value("_gitname", gitname, current_file, False, False)
        write_value('source', "{}::{}".format(gitname, gitroot), current_file)
        first += "\tmsg \"Connecting to $_gitname GIT server...\"\n"
        first += "\tif [ -d $startdir/src/$_gitname ] ; then\n"
        first += "\t\t(cd $_gitname && git pull origin )\n"
        first += "\telse \n"
        first += "\t\t(git clone $_gitroot && cd $_gitname)\n"
        first += "\tfi \n"
        first += "\tmsg \"GIT checkout done or server timeout\"\n"
        first += "\tcd $_gitname\n"
        sdir = "$_gitname"

    if build_method == "darcs":
        write_value("_darcsmod", ask_value("_darcsmod"), current_file, False, False)
        write_value("_darcstrunk", ask_value("_darcstrunk"), current_file, False, False)
        second = "\nprepare() {\n\tcd ${srcdir}\n"
        second += "\tmsg \"Checking for previous build\"\n"
        second += "\tif [ -d $startdir/src/$_darcsmod/_darcs ] ; then\n"
        second += "\t\tmsg \"Retrieving missing patches\"\n"
        second += "\t\t(cd $_darcsmod && darcs pull -a $_darcstrunk/$_darcsmod)\n"
        second += "\telse \n"
        second += "\t\tmsg \"Retrieving complete sources\"\n"
        second += "\t\t(darcs get --partial --set-scripts-executable $_darcstrunk/$_darcsmod && cd $_darcsmod)\n"
        second += "\tfi \n"
        second += "\tmsg \"Darcs checkout done or server timeout\"\n"
        current_file.write(second+'}')
        first += "\tcd $_darcsmod\n"
        sdir = "$_darcsmod"

    if build_method == "hg":
        hgroot = ask_value("_hgroot")
        hgrepo = ask_value("_hgrepo")
        write_value("_hgroot", hgroot, current_file, False, False)
        write_value("_hgrepo", hgrepo, current_file, False, False)
        write_value('source', "{}::{}".format(hgrepo, hgroot), current_file)
        first += "\tmsg \"Connecting to $_hgrepo HG server...\"\n"
        first += "\tif [ -d $startdir/src/$_hgrepo ] ; then\n"
        first += "\t\t(cd $_hgrepo && hg pull -u )\n"
        first += "\telse \n"
        first += "\t\t(hg clone ${_hgroot}/${_hgrepo} && cd $_hgrepo)\n"
        first += "\tfi \n"
        first += "\tmsg \"HG checkout done or server timeout\"\n"
        first += "\tcd $_hgrepo\n"
        sdir = "$_hgrepo"

    if build_method == "release":
        first += "\tcd $pkgname-$pkgver\n"
        sdir = "$pkgname-$pkgver"

    first += "\t#DON'T FORGET TO CONFIGURE ./autogen.sh --help-short\n"
    first += "\tmake\n"
    first += "}\npackage() {\n"
    first += "\tcd ${{srcdir}}/{}\n".format(sdir)
    first += "\tmake DESTDIR=${pkgdir} install\n"
    first += "\trm -rf ${pkgdir}/usr/share/man/{a*,b*,c*,d*,e*,f*,g*,h*,i*,j*,k*,l*,n*,o*,p*,q*,r*,s*,t*,u*,v*,w*,x*,y*,z*}\n"
    first += "\trm -rf ${pkgdir}/usr/share/locale/{a*,b*,c*,d*,e*,fa*,fb*,fc*,fd*,fe*,ff*,fg*,fh*,fi*,fj*,fk*,fl*,fm*,fn*,fo*,fp*,fq*,fs*,ft*,fu*,fv*,fw*,fx*,fy*,fz*,g*,h*,i*,j*,k*,l*,m*,n*,o*,p*,q*,r*,s*,t*,u*,v*,w*,x*,y*,z*}\n}\n"
    mk_pkgver(current_file, method)
    current_file.write(first)
    mk_vim_end(current_file)


FIELDS = ("pkgname", "pkgver", "pkgdesc", "url", "license", "install", "arch",
          "source", "noextract", "groups", "backup", "depends", "makedepends",
          "optdepends", "conflicts", "provides", "replaces", "options")
if __name__ == "__main__":
    PKGBUILD = open("PKGBUILD", "a")
    maintainer(PKGBUILD)
    for i in FIELDS:
        answer = None
        if i == "pkgname":
            answer = ask_value(i, os.popen("basename `pwd`").read().strip())
            method = get_update_method(answer)

        if i == "license":
            answer = ask_value(i, "GPL",
                      choice = ["Apache", "CDDL", "EPL", "GPL", "GPL3", "LGPL",
                                "LGPL3", "FDL", "MPL"])

        if i == "groups":
            answer = ask_value(i, os.popen("cd .. && basename `pwd`").read().strip())

        if i == "arch":
            answer = ask_value(i, os.popen("uname -m").read().strip())

        if i == "source":
            answer = ask_value(i, could_be_empty=True)
            if method == "release" or answer != "":
                write_value(i, answer, PKGBUILD, False, True)
                PKGBUILD.flush()
                #TODO Gerer les md5sums sur plusieurs lignes (quand plusieurs sources)
                write_value("md5sums", os.popen("makepkg -gm").read().strip()[10:42], \
                            PKGBUILD, True, True)

        if answer is None:
            if i in ("install", "source", "noextract", "groups", "backup",
                     "makedepends", "optdepends", "conflicts", "provides",
                     "replaces", "options"):
                answer = ask_value(i, could_be_empty=True)
            else:
                answer = ask_value(i)

        if answer != -1:
            if i in ("pkgname", "pkgver", "source"):
                need_quote = False
            else:
                need_quote = True

            if i in ("license", "install", "source", "noextract", "groups",
                     "arch", "backup", "depends", "makedepends", "optdepends",
                     "conflicts", "provides", "replaces", "options"):
                need_array = True
            else:
                need_array = False

            if i != "source":
                write_value(i, answer, PKGBUILD, need_quote, need_array)

            if i == "pkgver":
                write_value("pkgrel", "1", PKGBUILD, False, False)

        else:
            error(PKGBUILD)

    mk_build(PKGBUILD, method)
    PKGBUILD.close()
