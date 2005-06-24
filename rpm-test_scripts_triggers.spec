#
%define	_ver	%{!?ver:1}%{?ver:%ver}
#
Summary:	testing of rpm's scripts and triggers
Summary(pl):	testowanie skryptów i wyzwalaczy rpm'a
Name:		rpm-test_scripts_triggers
Version:	%{_ver}
Release:	0.1
Epoch:		0
License:	GPL
Group:		Development/Tools
Source0:	http://twittner.host.sk/files/%{name}/%{name}.tar.gz
# Source0-md5:	961d3479998c046fe2512e111bdd5b9b
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testing of rpm's scripts and triggers.

%description -l pl
testowanie skryptów i wyzwalaczy rpm'a.

%package first
Summary:	testing of rpm's scripts and triggers - first subpackage
Summary(pl):	testowanie skryptów i wyzwalaczy rpm'a - pierwszy podpakiet
Group:		Development/Tools
Obsoletes:	%{name}-second

%description first
testing of rpm's scripts and triggers - first subpackage which
obsoletes %{name}-second.

%description first -l pl
testowanie skryptów i wyzwalaczy rpm'a - pierwszy podpakiet obsoletuj±cy
%{name}-second.

%package second
Summary:	testing of rpm's scripts and triggers - second subpackage
Summary(pl):	testowanie skryptów i wyzwalaczy rpm'a - drugi podpakiet
Group:		Development/Tools
Obsoletes:	%{name}-first

%description second
testing of rpm's scripts and triggers - second subpackage which
obsoletes %{name}-first.

%description second -l pl
testowanie skryptów i wyzwalaczy rpm'a - drugi podpakiet obsoletuj±cy
%{name}-first.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

###########################################################
%pre
echo '#MAIN PACKAGE#' pre: \$1: ${1}, \$2: $2

%post
echo '#MAIN PACKAGE#' post: \$1: ${1}, \$2: $2

%preun
echo '#MAIN PACKAGE#' preun: \$1: ${1}, \$2: $2

%postun
echo '#MAIN PACKAGE#' postun: \$1: ${1}, \$2: $2

###########################################################
%pre first
echo '#FIRST SUBPACKAGE#' pre: \$1: ${1}, \$2: $2

%post first
echo '#FIRST SUBPACKAGE#' post: \$1: ${1}, \$2: $2

%preun first
echo '#FIRST SUBPACKAGE#' preun: \$1: ${1}, \$2: $2

%postun first
echo '#FIRST SUBPACKAGE#' postun: \$1: ${1}, \$2: $2

###########################################################
%pre second
echo '#SECOND SUBPACKAGE#' pre: \$1: ${1}, \$2: $2

%post second
echo '#SECOND SUBPACKAGE#' post: \$1: ${1}, \$2: $2

%preun second
echo '#SECOND SUBPACKAGE#' preun: \$1: ${1}, \$2: $2

%postun second
echo '#SECOND SUBPACKAGE#' postun: \$1: ${1}, \$2: $2

###########################################################
%triggerin -- %{name}
echo '#MAIN PACKAGE#' triggerin: \$1: ${1}, \$2: $2

%triggerun -- %{name}
echo '#MAIN PACKAGE#' triggerun: \$1: ${1}, \$2: $2

%triggerpostun -- %{name}
echo '#MAIN PACKAGE#' triggerpostun: \$1: ${1}, \$2: $2

###########################################################
%triggerin first -- %{name}-second
echo '#FIRST SUBPACKAGE#' triggerin: \$1: ${1}, \$2: $2

%triggerun first -- %{name}-second
echo '#FIRST SUBPACKAGE#' triggerun: \$1: ${1}, \$2: $2

%triggerpostun first -- %{name}-second
echo '#FIRST SUBPACKAGE#' triggerpostun: \$1: ${1}, \$2: $2

###########################################################
%triggerin second -- %{name}-first
echo '#SECOND SUBPACKAGE#' triggerin: \$1: ${1}, \$2: $2

%triggerun second -- %{name}-first
echo '#SECOND SUBPACKAGE#' triggerun: \$1: ${1}, \$2: $2

%triggerpostun second -- %{name}-first
echo '#SECOND SUBPACKAGE#' triggerpostun: \$1: ${1}, \$2: $2

###########################################################

%files
%defattr(644,root,root,755)
%doc README

%files first
%defattr(644,root,root,755)
%doc README

%files second
%defattr(644,root,root,755)
%doc README
