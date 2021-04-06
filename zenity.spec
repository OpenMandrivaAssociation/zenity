%define url_ver %(echo %{version} | cut -d "." -f -2)
%define _disable_rebuild_configure 1

Name:		zenity
Summary:	Call GNOME dialog boxes from the command line
Version:	3.32.0
Release:	4
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool itstool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libnotify) >= 0.6.1
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	libxslt-proc
BuildRequires:	libxml2-utils
BuildRequires:	yelp-tools

Requires(post,preun): update-alternatives

%description
Zenity allows you to display dialog boxes from the commandline and shell
scripts.

# Main binary package renamed to zenity-gtk so 3rd party packages
# that use Requires: zenity can pull in qarma instead (users can still
# install and prefer zenity-gtk)
%package gtk
Summary: Call GNOME dialog boxes from the command line
Requires(post,preun):	update-alternatives

%description gtk
Call GNOME dialog boxes from the command line

%prep
%autosetup -p1

%build
%configure
%make_build
										
%install
rm -rf %{buildroot} %{name}-0.1.lang

%make_install

%find_lang %{name}-0.1 --with-gnome --all-name

# Move it aside so people who prefer Qt can use Qarma
# The alternatives system takes care of the rest.
mv %{buildroot}%{_bindir}/zenity %{buildroot}%{_bindir}/zenity-gtk

%post gtk
%{_sbindir}/update-alternatives --install %{_bindir}/zenity zenity %{_bindir}/zenity-gtk 1

%preun gtk
%{_sbindir}/update-alternatives --remove zenity %{_bindir}/zenity-gtk

%files gtk -f %{name}-0.1.lang
%doc AUTHORS COPYING HACKING NEWS README THANKS TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
