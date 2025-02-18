#
# Conditional build:
%bcond_with	gnutls	# GnuTLS instead of OpenSSL for encryption
%bcond_without	openssl	# OpenSSL encryption support

%if %{with gnutls}
%undefine	with_openssl
%endif
Summary:	Intel AMT serial-over-lan (sol) client
Summary(pl.UTF-8):	Klient portu szeregowego po sieci (SOL) Intel AMT
Name:		amtterm
Version:	1.7
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	https://www.kraxel.org/releases/amtterm/%{name}-%{version}.tar.gz
# Source0-md5:	c8ab796464e11df115d82d39f30f28b1
URL:		https://www.kraxel.org/blog/linux/amtterm/
%{?with_gnutls:BuildRequires:	gnutls-devel}
BuildRequires:	gtk+3-devel >= 3.0
%{?with_openssl:BuildRequires:	openssl-devel}
BuildRequires:	pkgconfig
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	vte-devel >= 0.38
# for amttool
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
	%{?with_gnutls:USE_GNUTLS=1} \
	%{?with_openssl:USE_OPENSSL=1} \
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
%attr(755,root,root) %{_bindir}/amtider
%attr(755,root,root) %{_bindir}/amtterm
%attr(755,root,root) %{_bindir}/amttool
%{_mandir}/man1/amtider.1*
%{_mandir}/man1/amtterm.1*
%{_mandir}/man1/amttool.1*
%{_mandir}/man7/amt-howto.7*

%files -n gamt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gamt
%{_mandir}/man1/gamt.1*
%{_desktopdir}/gamt.desktop
