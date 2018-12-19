# One test fails on all arches, and two on arm. Issue filed:
# https://github.com/WoLpH/python-progressbar/issues/182
%bcond_with tests

%global srcname progressbar2

%global desc %{expand: \
A text progress bar is typically used to display the progress of a long running
operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of the line
is given by a number of widgets.

The progressbar module is very easy to use, yet very powerful. It will also
automatically enable features like auto-resizing when the system supports it.}

Name:           python-%{srcname}
Version:        3.38.0
Release:        1%{?dist}
Summary:        A Progressbar library to provide visual progress to long running operations


License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:  %{py3_dist python-utils}
Requires:  %{py3_dist six}
BuildRequires:  %{py3_dist python-utils}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist pytest-cache}
BuildRequires:  %{py3_dist pytest-runner}
BuildRequires:  %{py3_dist pytest-flakes}
BuildRequires:  %{py3_dist pytest-cache}
BuildRequires:  %{py3_dist pytest-pep8}
BuildRequires:  %{py3_dist flake8}
%if %{with tests}
BuildRequires:  %{py3_dist freezegun} >= 0.3.10
%endif

# obsolete python-progressbar
Obsoletes:      python3-progressbar < 2.3-14

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%autosetup -n %{srcname}-%{version}
rm -rfv %{srcname}.egg-info

find . -name '*.pyc' -print -delete
find . -name '*.swp' -print -delete
rm -rfv tests/__pycache__/

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst CONTRIBUTING.rst
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info
%{python3_sitelib}/progressbar

%changelog
* Thu Dec 13 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.38.0-1
- Check tests and file issue upstream
- Initial build
- Drop py2 subpackage
- Obsolete python-progressbar
