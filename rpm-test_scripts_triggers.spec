Summary:	Testing of rpm's scripts and triggers
Name:		rpm-foo
Version:	0.1
Release:	0.9
Epoch:		0
License:	GPL
Group:		Development/Tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
test

%prep

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans
set -x
echo pretrans called! %{name} %{epoch}:%{version}-%{release}
touch /tmp/pretrans

%posttrans -p /bin/sh
set -x
echo >&2 "foo foo"
echo posttrans called! %{name} %{epoch}:%{version}-%{release}
touch /tmp/posttrans

%files
%defattr(644,root,root,755)
