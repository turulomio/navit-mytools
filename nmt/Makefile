DESTDIR ?= /

PREFIXETC=$(DESTDIR)/etc/conf.d/
PREFIXINITD=$(DESTDIR)/etc/init.d/
PREFIXBIN=$(DESTDIR)/usr/bin
PREFIXSHARE=$(DESTDIR)/usr/share/navit-mytools

install:
	install -o root -d $(PREFIXBIN)
	install -o root -d $(PREFIXSHARE)
	install -o root -d $(PREFIXINITD)
	install -o root -d $(PREFIXETC)
	install -m 755 -o root geopositioning.py $(PREFIXBIN)/nmt-geopositioning
	install -m 755 -o root geopositioning-audio.py $(PREFIXBIN)/nmt-geopositioning-audio
	install -m 755 -o root navit-config.py $(PREFIXBIN)/nmt-navit-config
	install -m 755 -o root navit-map-geoname.py $(PREFIXBIN)/nmt-map-geoname
	install -m 755 -o root navit-map-point.py $(PREFIXBIN)/nmt-map-point
	install -m 755 -o root navit-sort-bookmarks.py $(PREFIXBIN)/nmt-navit-sort-bookmarks
	install -m 755 -o root osm-download.py $(PREFIXBIN)/nmt-osm-download
	install -m 755 -o root system.py $(PREFIXBIN)/nmt-system
	install -m 755 -o root navit-reboot.py $(PREFIXBIN)/nmt-navit-reboot
	install -m 755 -o root gps-status.py $(PREFIXBIN)/nmt-system-status
	install -m 644 -o root libnavitmytools.py $(PREFIXSHARE)
	install -m 644 -o root nmt-system.confd $(PREFIXETC)/nmt-system.default
	install -m 755 -o root nmt-system.initd $(PREFIXINITD)/nmt-system
uninstall:
	rm $(PREFIXBIN)/nmt-*
	rm -Rf $(PREFIXSHARE)
