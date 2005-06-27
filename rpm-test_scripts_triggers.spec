#
%define	_ver	%{!?ver:1}%{?ver:%ver}
#
Summary:	Testing of rpm's scripts and triggers
Summary(pl):	Testowanie skryptów i wyzwalaczy rpm-a
Name:		rpm-test_scripts_triggers
Version:	%{_ver}
Release:	0.1
Epoch:		0
License:	GPL
Group:		Development/Tools
Source0:	http://twittner.host.sk/files/rpm-test_scripts_triggers/%{name}.tar.gz
# Source0-md5:	961d3479998c046fe2512e111bdd5b9b
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_nvr	%{name}-%{version}-%{release}
%define	_nfvr	%{name}-first-%{version}-%{release}
%define	_nsvr	%{name}-second-%{version}-%{release}

%description
Testing of rpm's scripts and triggers.

%description -l pl
Testowanie skryptów i wyzwalaczy rpm-a.

%package first
Summary:	Testing of rpm's scripts and triggers - first subpackage
Summary(pl):	Testowanie skryptów i wyzwalaczy rpm-a - pierwszy podpakiet
Group:		Development/Tools
Obsoletes:	%{name}-second

%description first
Testing of rpm's scripts and triggers - first subpackage which
obsoletes %{name}-second.

%description first -l pl
Testowanie skryptów i wyzwalaczy rpm-a - pierwszy podpakiet obsoletuj±cy
%{name}-second.

%package second
Summary:	Testing of rpm's scripts and triggers - second subpackage
Summary(pl):	Testowanie skryptów i wyzwalaczy rpm-a - drugi podpakiet
Group:		Development/Tools
Obsoletes:	%{name}-first

%description second
Testing of rpm's scripts and triggers - second subpackage which
obsoletes %{name}-first.

%description second -l pl
Testowanie skryptów i wyzwalaczy rpm-a - drugi podpakiet obsoletuj±cy
%{name}-first.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

echo nothing interesting here > config.conf

install -D config.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/config.conf
install -D config.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}-first/config.conf
install -D config.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}-second/config.conf

%clean
rm -rf $RPM_BUILD_ROOT

###########################################################
%pre
echo %{_nvr} pre: \$1: ${1}, \$2: $2

%post
echo  %{_nvr} post: \$1: ${1}, \$2: $2
echo 'config changed' | tee -a %{_sysconfdir}/%{name}/config.conf

%preun
echo %{_nvr} preun: \$1: ${1}, \$2: $2

%postun
echo %{_nvr} postun: \$1: ${1}, \$2: $2

###########################################################
%pre first
echo %{_nfvr} pre: \$1: ${1}, \$2: $2

%post first
echo %{_nfvr} post: \$1: ${1}, \$2: $2
echo 'config changed' | tee -a %{_sysconfdir}/%{name}-first/config.conf

%preun first
echo %{_nfvr} preun: \$1: ${1}, \$2: $2

%postun first
echo %{_nfvr} postun: \$1: ${1}, \$2: $2

###########################################################
%pre second
echo %{_nsvr} pre: \$1: ${1}, \$2: $2

%post second
echo %{_nsvr} post: \$1: ${1}, \$2: $2
echo 'config changed' | tee -a %{_sysconfdir}/%{name}-second/config.conf

%preun second
echo %{_nsvr} preun: \$1: ${1}, \$2: $2

%postun second
echo %{_nsvr} postun: \$1: ${1}, \$2: $2

###########################################################
%triggerin -- %{name} < %{version}-%{release}
echo %{_nvr} triggerin: \$1: ${1}, \$2: $2

%triggerun -- %{name} < %{version}-%{release}
echo %{_nvr} triggerun: \$1: ${1}, \$2: $2

%triggerpostun -- %{name} < %{version}-%{release}
echo %{_nvr} triggerpostun: \$1: ${1}, \$2: $2

###########################################################
%triggerin first -- %{name}-second
echo %{_nfvr} triggerin: \$1: ${1}, \$2: $2

%triggerun first -- %{name}-second
echo %{_nfvr} triggerun: \$1: ${1}, \$2: $2

%triggerpostun first -- %{name}-second
echo %{_nfvr} triggerpostun: \$1: ${1}, \$2: $2

###########################################################
%triggerin second -- %{name}-first
echo %{_nsvr} triggerin: \$1: ${1}, \$2: $2

%triggerun second -- %{name}-first
echo %{_nsvr} triggerun: \$1: ${1}, \$2: $2

%triggerpostun second -- %{name}-first
echo %{_nsvr} triggerpostun: \$1: ${1}, \$2: $2

###########################################################

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/config.conf

%files first
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}-first/config.conf

%files second
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}-second/config.conf
