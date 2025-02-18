Summary:	Intel AMT serial-over-lan (sol) client
Summary(pl.UTF-8):	Klient portu szeregowego po sieci (SOL) Intel AMT
Name:		amtterm
Version:	1.3
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.kraxel.org/releases/amtterm/%{name}-%{version}.tar.gz
# Source0-md5:	a2385b2305680ae06687867527924ff5
Patch0:		amtterm-reconnect-hack.patch
URL:		http://www.kraxel.org/blog/linux/amtterm/
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	vte0-devel
Requires:	perl-SOAP-Lite
Requires:	perl-SOAP-Lite-HTTP
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serial-over-lan (sol) client for Intel AMT.

%description -l pl.UTF-8
Klient portu szeregowego po sieci (SOL - Serial-over-LAN) Intel AMT.

%package -n gamt
Summary:	Graphical Intel AMT serial-over-lan (sol) client
Summary(pl.UTF-8):	Graficzny klient portu szeregowego po sieci (SOL) Intel AMT
Group:		X11/Applications/Networking

%description -n gamt
Serial-over-lan (sol) client for Intel AMT.

This package contains graphical (GTK+) version.

%description -n gamt -l pl.UTF-8
Klient portu szeregowego po sieci (SOL - Serial-over-LAN) Intel AMT.

Ten pakiet zawiera wersję graficzną (GTK+).

%prep
%setup -q
%patch -P0 -p1

%build
# note: force LIB= because check is error-prone, e.g. existence of
# piplib (libpiplib64.so) or polylib (libpolylib64.so) causes to use lib64
# on 32-bit system
prefix=%{_prefix} \
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
STRIP=" " \
%{__make} \
	LIB=%{_lib} \
	verbose=yes

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/amtterm
%attr(755,root,root) %{_bindir}/amttool
%{_mandir}/man1/amtterm.1*
%{_mandir}/man1/amttool.1*
%{_mandir}/man7/amt-howto.7*

%files -n gamt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gamt
%{_mandir}/man1/gamt.1*
%{_desktopdir}/gamt.desktop
