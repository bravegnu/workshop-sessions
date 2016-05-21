TOPDIR = ../

EXPORT_WIDTH  = 1024

images_dia = $(wildcard figures/*.dia)
images_png = $(images_dia:.dia=.png)
datauris = code/csum/csum.full.datauri        \
	   code/startup/startup.full.datauri  \
	   code/syscalls/syscalls.full.datauri

code/csum/csum.full.datauri: MIMETYPE="text/plain;charset=us-ascii"

code/startup/startup.full.datauri: MIMETYPE="text/plain;charset=us-ascii"

code/syscalls/syscalls.full.datauri: MIMETYPE="text/plain;charset=us-ascii"

all: csum-lds-split startup-split syscalls-split slides.html

csum-lds-split:
	python $(TOPDIR)/scripts/split.py code/csum.lds

startup-split:
	python $(TOPDIR)/scripts/split.py code/startup.s

syscalls-split:
	python $(TOPDIR)/scripts/split.py code/syscalls.c

slides.html: $(images_png) $(datauris)

clean:
	rm -f $(images_png)
	rm -f $(datauris)
	rm -f slides.html
	rm -rf code/csum
	rm -rf code/startup
	rm -rf code/syscalls

include $(TOPDIR)/stylesheets/Makefile.rules