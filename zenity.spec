Name:		zenity
Summary:	Call GNOME dialog boxes from the command line
Version:	3.4.0
Release:	1
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	intltool
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

