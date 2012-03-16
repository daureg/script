prefix			= ${DESTDIR}/usr
bindir			= ${prefix}/bin
INSTALL_bin		= install -D -m755

install:
	$(INSTALL_bin) add_grub_entry.py ${bindir}/add_grub_entry 
	$(INSTALL_bin) check_python.sh ${bindir}/check_python
	$(INSTALL_bin) fbsetbg.sh ${bindir}/fbsetbg # http://git.fluxbox.org/fluxbox.git/plain/util/fbsetbg
	$(INSTALL_bin) get_sysinfo.py ${bindir}/get_sysinfo
	$(INSTALL_bin) icatalyst.sh ${bindir}/icatalyst
	$(INSTALL_bin) iradeon.sh ${bindir}/iradeon
	$(INSTALL_bin) npkg.py ${bindir}/npkg
	$(INSTALL_bin) pkg-install.py ${bindir}/pkg-install
	$(INSTALL_bin) pks.py ${bindir}/pks
	$(INSTALL_bin) post_song.py ${bindir}/post_song
	$(INSTALL_bin) pysay.py ${bindir}/pysay
	$(INSTALL_bin) save_pkg.py ${bindir}/save_pkg
	$(INSTALL_bin) screenshot.pl ${bindir}/screenshot
	$(INSTALL_bin) texplate.py ${bindir}/texplate
	$(INSTALL_bin) twenty_minutes.py ${bindir}/20minutes
	$(INSTALL_bin) unwanted_modules.py ${bindir}/unwanted_modules
	$(INSTALL_bin) updir.py ${bindir}/updir
	$(INSTALL_bin) writepkg.py ${bindir}/writepkg

uninstall:
	rm ${bindir}/add_grub_entry 
	rm ${bindir}/check_python
	rm ${bindir}/fbsetbg
	rm ${bindir}/get_sysinfo
	rm ${bindir}/icatalyst
	rm ${bindir}/iradeon
	rm ${bindir}/npkg
	rm ${bindir}/pkg-install
	rm ${bindir}/pks
	rm ${bindir}/post_song
	rm ${bindir}/pysay
	rm ${bindir}/save_pkg
	rm ${bindir}/screenshot
	rm ${bindir}/texplate
	rm ${bindir}/20minutes
	rm ${bindir}/unwanted_modules
	rm ${bindir}/updir
	rm ${bindir}/writepkg
