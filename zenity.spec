Name: zenity
Summary: Call GNOME dialog boxes from the command line
Version: 2.20.1
Release: %mkrel 1
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}
License:	GPL
Group:		Development/GNOME and GTK+
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libglade2.0-devel
BuildRequires:  libGConf2-devel libgnomecanvas2-devel
BuildRequires:  scrollkeeper
BuildRequires:  gtk+2-devel >= 2.9.0
BuildRequires:	perl-XML-Parser
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libxslt-proc
Requires(post):		scrollkeeper >= 0.3
Requires(postun):		scrollkeeper >= 0.3
Conflicts: gnome-utils < 2.3.3
Provides: xmsg-dialog

%description
Zenity allows you to display dialog boxes from the commandline and shell
scripts.

%prep
%setup -q

%build

%configure2_5x --disable-scrollkeeper

%make
										
%install
rm -rf $RPM_BUILD_ROOT %name-0.1.lang

%makeinstall_std


%find_lang %name-0.1 --with-gnome --all-name
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-0.1.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper

%files -f %name-0.1.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README THANKS TODO
%{_bindir}/*
%{_datadir}/%{name}
%dir %{_datadir}/omf/%{name}
%{_datadir}/omf/%{name}/%name-C.omf
%{_mandir}/man1/*
