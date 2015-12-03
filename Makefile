NAME=Tuxpaint.activity
all:

install: all
	install -d $(DESTDIR)/usr/share/sugar/activities/${NAME}/
	install -m 744  activity.py $(DESTDIR)/usr/share/sugar/activities/${NAME}/
	install -m 744  tuxpaint-import.sh $(DESTDIR)/usr/share/sugar/activities/${NAME}/
	install -d $(DESTDIR)/usr/share/sugar/activities/${NAME}/activity
	install -m 744  activity/* $(DESTDIR)/usr/share/sugar/activities/${NAME}/activity/
