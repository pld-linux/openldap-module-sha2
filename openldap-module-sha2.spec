
%define		svnrel	37261
Summary:	Support for SHA-512, SHA-384 and SHA-256 hashed passwords in OpenLDAP
Summary(pl.UTF-8):	Obsługa haseł SHA-512, SHA-384 and SHA-256 dla OpenLDAP
Name:		openldap-module-sha2
Version:	0.%{svnrel}
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://xatka.net/~z/PLD/%{name}-%{svnrel}.tar.bz2
# Source0-md5:	56e27d51467898783da461c4f0c78091
Source1:	%{name}.make
URL:		http://confluence.atlassian.com/display/JIRAEXT/OpenLDAP+support+for+SHA-2+%28SHA-256,+SHA-384,+SHA-512%29+and+atlassian-sha1+passwords
BuildRequires:	openldap-headers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Support for SHA-512, SHA-384 and SHA-256 hashed passwords in OpenLDAP.

%description -l pl.UTF-8
Obsługa haseł SHA-512, SHA-384 and SHA-256 dla OpenLDAP.

%prep
%setup -qn %{name}-%{svnrel}

%build
%{__make} -f %{SOURCE1} OPENLDAPINC=%{_includedir}/openldap
%{__make} -C standalone

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/openldap,%{_bindir}}
cp slapd-sha2.so $RPM_BUILD_ROOT%{_libdir}/openldap/slapd-sha2.so
cp standalone/sha2print $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/openldap/slapd-sha2.so
%{_bindir}/sha2print
