prefix			= ${DESTDIR}/usr
bindir			= ${prefix}/bin
INSTALL_bin		= install -D -m755

install:
	$(INSTALL_bin) add_grub_entry.py ${bindir}/add_grub_entry 
	$(INSTALL_bin) bacman.sh ${bindir}/bacman # http://projects.archlinux.org/pacman.git/plain/contrib/bacman
	$(INSTALL_bin) bench3d.sh ${bindir}/bench3d
	$(INSTALL_bin) check_python.sh ${bindir}/check_python
	$(INSTALL_bin) fbsetbg.sh ${bindir}/fbsetbg # http://git.fluxbox.org/?p=fluxbox.git;a=blob_plain;f=util/fbsetbg;hb=HEAD
	$(INSTALL_bin) gastyle.sh ${bindir}/gastyle
	$(INSTALL_bin) get_sysinfo.py ${bindir}/get_sysinfo
	$(INSTALL_bin) icatalyst.sh ${bindir}/icatalyst
	$(INSTALL_bin) iradeon.sh ${bindir}/iradeon
	$(INSTALL_bin) npkg.py ${bindir}/npkg
	$(INSTALL_bin) pactree.sh ${bindir}/pactree # http://projects.archlinux.org/gitweb.cgi?p=pacman.git;a=blob_plain;f=contrib/pactree;hb=HEAD
	$(INSTALL_bin) pkg-install.py ${bindir}/pkg-install
	$(INSTALL_bin) pks.py ${bindir}/pks
	$(INSTALL_bin) post_song.py ${bindir}/post_song
	$(INSTALL_bin) pysay.py ${bindir}/pysay
	$(INSTALL_bin) save_pkg.py ${bindir}/save_pkg
	$(INSTALL_bin) screenshot.pl ${bindir}/screenshot
	$(INSTALL_bin) twenty_minutes.py ${bindir}/20minutes
	$(INSTALL_bin) unwanted_modules.py ${bindir}/unwanted_modules
	$(INSTALL_bin) updir.py ${bindir}/updir
	$(INSTALL_bin) writepkg.py ${bindir}/writepkg
