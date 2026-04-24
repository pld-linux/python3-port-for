#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Utility that helps with local TCP ports management
Summary(pl.UTF-8):	Narzędzie pomagające zarządzać lokalnymi portami TCP
Name:		python3-port-for
Version:	1.0.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/port-for/
Source0:	https://files.pythonhosted.org/packages/source/p/port-for/port_for-%{version}.tar.gz
# Source0-md5:	f2c31f7fe0a29577ecdb4daf1e777add
URL:		https://pypi.org/project/port-for/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools >= 1:61
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
port-for is a command-line utility and a python library that helps with
local TCP ports management. It can find an unused TCP localhost port and
remember the association.

%description -l pl.UTF-8
port-for to narzędzie uruchamiane z linii poleceń oraz biblioteka
pythonowa pomagająca w zarządzaniu lokalnymi portami TCP. Potrafi
znaleźć nieużywany port lokalny TCP i zapamiętać skojarzenie.

%prep
%setup -q -n port_for-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst
%attr(755,root,root) %{_bindir}/port-for
%{py3_sitescriptdir}/port_for
%{py3_sitescriptdir}/port_for-%{version}.dist-info
