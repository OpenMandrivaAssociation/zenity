Name:		zenity
Summary:	Call GNOME dialog boxes from the command line
Version:	3.7.2
Release:	8
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.7/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool itstool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libnotify) >= 0.6.1
BuildRequires:	pkgconfig(x11)

%description
Zenity allows you to display dialog boxes from the commandline and shell
scripts.

%prep
%setup -q

%build
%configure2_5x --disable-scrollkeeper
%make
										
%install
rm -rf %{buildroot} %{name}-0.1.lang

%makeinstall_std

%find_lang %{name}-0.1 --with-gnome --all-name

%files -f %{name}-0.1.lang
%doc AUTHORS COPYING HACKING NEWS README THANKS TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*



%changelog
* Tue Oct  9 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.0-1
+ Revision: 794371
- version update 3.4.0

* Fri Mar 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0-1
+ Revision: 783430
- new version 3.2.0
- cleaned up spec

* Thu Apr 07 2011 Funda Wang <fwang@mandriva.org> 2.32.1-2
+ Revision: 651435
- BR gnome-common
- add upstream patch to build with libnotify 0.7

* Mon Nov 15 2010 Götz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 597868
- update to new version 2.32.1

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581787
- update to new version 2.32.0

* Tue Sep 14 2010 Götz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 578143
- update to new version 2.31.92

* Thu Aug 05 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 566252
- new version
- update build deps

* Mon Mar 29 2010 Funda Wang <fwang@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528712
- update to new version 2.30.0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-3mdv2010.1
+ Revision: 524480
- rebuilt for 2010.1

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Fix mixed-use-of-spaces-and-tabs

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 2.28.0-2mdv2010.0
+ Revision: 454733
- do not package huge ChangeLog

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446700
- update to new version 2.28.0

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414696
- update to new version 2.27.90

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356262
- update to new version 2.26.0

* Tue Jan 13 2009 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 328858
- update to new version 2.24.1

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287358
- new version

* Fri Jul 18 2008 Götz Waschk <waschk@mandriva.org> 2.23.3.1-1mdv2009.0
+ Revision: 238066
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.3-1mdv2009.0
+ Revision: 231150
- new version
- fix license
- update deps

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192471
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183386
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 175065
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 113312
- new version

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.20.0-2mdv2008.0
+ Revision: 90399
- rebuild

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.19.2-1mdv2008.0
+ Revision: 63210
- new version

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 2.19.1-2mdv2008.0
+ Revision: 36222
- rebuild with correct optflags

  + Götz Waschk <waschk@mandriva.org>
    - new version

* Mon May 28 2007 Götz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 32176
- new version

* Wed Apr 18 2007 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 14378
- new version

