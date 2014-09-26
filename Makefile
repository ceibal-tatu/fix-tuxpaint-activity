NAME=Tuxpaint.activity
all:

install: all
	install -d $(DESTDIR)/home/ceibal/Activities/${NAME}/
	install -m 744  activity.py $(DESTDIR)/home/ceibal/Activities/${NAME}/
	install -m 744  tuxpaint-import.sh $(DESTDIR)/home/ceibal/Activities/${NAME}/
	install -d $(DESTDIR)/home/ceibal/Activities/${NAME}/activity
	install -m 744  activity/* $(DESTDIR)/home/ceibal/Activities/${NAME}/activity/
