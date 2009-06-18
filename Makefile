include MCONFIG_ALL
CWD=$(shell pwd)

default:: all

all:
	cd tcm-py ; python setup.py install
	cd lio-py ; python setup.py install
	-if test -d tools; then make -C tools; fi;
ifeq ($(SNMP_FEATURE), 1)
	-if test -d mib-modules; then make -C mib-modules; fi;
endif

install: all
	cd tcm-py ; sh install.sh
	cd lio-py ; sh install.sh
	-if test -d tools; then make -C tools install; fi
ifeq ($(SNMP_FEATURE), 1)
	-if test -d mib-modules; then make -C mib-modules install; fi
endif
	if [ ! -d $(DESTDIR)/etc/init.d ]; then		\
		mkdir -p $(DESTDIR)/etc/init.d;		\
	fi
	install -m 0755 $(CWD)/scripts/rc.target $(DESTDIR)/etc/init.d/target
	if [ ! -d $(DESTDIR)/etc/target ]; then		\
		mkdir -p $(DESTDIR)/etc/target;		\
	fi

deinstall:
	cd tcm-py ; uninstall.sh
	cd lio-py ; uninstall.sh

clean:
	cd tcm-py ; python setup.py clean
	cd lio-py ; python setup.py clean
	rm -rf build
	-if test -d tools; then make -C tools clean; fi;
ifeq ($(SNMP_FEATURE), 1)
	-if test -d mib-modules; then make -C mib-modules clean; fi;
endif