TOPDIR = ../

EXPORT_WIDTH  = 1024

images_dia = $(wildcard figures/*.dia)
images_png = $(images_dia:.dia=.png)

all: slides.html

slides.html: $(images_png) 

clean:
	rm -f $(images_png)
	rm -f slides.html
	rm -fr code/simple

include $(TOPDIR)/stylesheets/Makefile.rules
