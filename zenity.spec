%define url_ver %(echo %{version} | cut -d "." -f -2)
%define _disable_rebuild_configure 1

Name:		zenity
Summary:	Call GNOME dialog boxes from the command line
Version:	4.0.2
Release:	4
License:	LGPLv2+
Group:		Development/GNOME and GTK+
URL:		https://download.gnome.org/sources/zenity/
Source0:	https://download.gnome.org/sources/zenity/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool itstool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libnotify) >= 0.6.1
BuildRequires:	pkgconfig(webkitgtk-6.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	libxslt-proc
BuildRequires:	libxml2-utils
BuildRequires:	yelp-tools
#BuildRequires:	x11-server-xvfb

Recommends: zenity-wrapper

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
%meson	\
	-Dmanpage=false \
	-Dwebkitgtk=true
%meson_build
										
%install
rm -rf %{buildroot} %{name}-0.1.lang

%meson_install

%find_lang %{name}-0.1 --with-gnome --all-name

# Move it aside so people who prefer Qt can use Qarma
# The alternatives system takes care of the rest.
mv %{buildroot}%{_bindir}/zenity %{buildroot}%{_bindir}/zenity-gtk

%files gtk -f %{name}-0.1.lang
%doc AUTHORS COPYING NEWS README*
%{_bindir}/*
%{_datadir}/applications/org.gnome.Zenity.desktop
%{_iconsdir}/hicolor/*x*/apps/zenity.png
