Name:		zenity
Summary:	Call GNOME dialog boxes from the command line
Version:	2.32.1
Release:	%mkrel 2
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		zenity-2.32.1-libnotify0.7.patch
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}
License:	LGPLv2+
Group:		Development/GNOME and GTK+
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libnotify-devel
BuildRequires:	scrollkeeper
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	libxslt-proc
Conflicts:	gnome-utils < 2.3.3
Provides:	xmsg-dialog

%description
Zenity allows you to display dialog boxes from the commandline and shell
scripts.

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --disable-scrollkeeper
%make
										
%install
rm -rf %{buildroot} %name-0.1.lang

%makeinstall_std

%find_lang %name-0.1 --with-gnome --all-name
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-0.1.lang
done

%clean
rm -rf %{buildroot}

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper

%files -f %name-0.1.lang
%defattr(-,root,root)
%doc AUTHORS COPYING HACKING NEWS README THANKS TODO
%{_bindir}/*
%{_datadir}/%{name}
%dir %{_datadir}/omf/%{name}
%{_datadir}/omf/%{name}/%name-C.omf
%{_mandir}/man1/*
