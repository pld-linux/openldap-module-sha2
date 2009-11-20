
%define		svnrel	37261
Summary:	Support for SHA-512, SHA-384 and SHA-256 hashed passwords in OpenLDAP
Summary(pl.UTF-8):	Obsługa haseł SHA-512, SHA-384 and SHA-256 dla OpenLDAP
Name:		openldap-module-sha2
Version:	0.%{svnrel}
Release:	1
License:	BSD
Group:		Applications
Source0:	http://xatka.net/~z/PLD/%{name}-%{svnrel}.tar.bz2
# Source0-md5:	56e27d51467898783da461c4f0c78091
URL:		http://confluence.atlassian.com/display/JIRAEXT/OpenLDAP+support+for+SHA-2+%28SHA-256,+SHA-384,+SHA-512%29+and+atlassian-sha1+passwords
BuildRequires:	openldap-headers
Patch0:		%{name}-link.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Support for SHA-512, SHA-384 and SHA-256 hashed passwords in OpenLDAP.

%description -l pl.UTF-8
Obsługa haseł SHA-512, SHA-384 and SHA-256 dla OpenLDAP.

%prep
%setup -qn %{name}-%{svnrel}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags} -fPIC -I%{_includedir}/openldap" \
	LDFLAGS="%{rpmldflags}"
%{__make} -C standalone \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/openldap,%{_bindir}}
install -p slapd-sha2.so $RPM_BUILD_ROOT%{_libdir}/openldap/slapd-sha2.so
install -p standalone/sha2print $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/openldap/slapd-sha2.so
%attr(755,root,root) %{_bindir}/sha2print
