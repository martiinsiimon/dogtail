Name:		dogtail3
Version:	0.9.0
Release:	4.beta1
Summary:	GUI testing tool and automation framework. Python3 compatible version.

License:	GPLv2
URL:		http://dogtail.fedorahosted.org/
Source0:	dist/%{name}-%{version}-%{release}.tar.gz

BuildArch:  noarch

BuildRequires:	python3-devel

Requires: python3-pyatspi
Requires: python3-gobject
Requires: python3-cairo
Requires: rpm-python3
Requires: xorg-x11-xinit


%description
GUI test tool and automation framework that uses assistive technologies to
communicate with desktop applications. Python3 compatible version.

%prep
%setup -q -n %{name}-%{version}-%{release}


%build
python3 ./setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python3 ./setup.py install -O2 --root=$RPM_BUILD_ROOT --record=%{name}.files
rm -rf $RPM_BUILD_ROOT/%{_docdir}/dogtail3
find examples -type f -exec chmod 0644 \{\} \;
desktop-file-install $RPM_BUILD_ROOT/%{_datadir}/applications/sniff3.desktop \
  --vendor=fedora \
  --dir=$RPM_BUILD_ROOT/%{_datadir}/applications \
  --add-category X-Fedora \
  --delete-original


%clean
rm -rf $RPM_BUILD_ROOT

%files
#%defattr(-,root,root,-)
%{_bindir}/*
%{python3_sitelib}/dogtail/
%{python3_sitelib}/*.egg-info
%{_datadir}/applications/*
%{_datadir}/dogtail3/
%{_datadir}/icons/hicolor/*
%doc COPYING
%doc README
%doc NEWS
%doc dogtail3.spec
%doc examples/


%changelog
* Sat Aug 02 2014 Martin Simon <martiin.siimon@gmail.com> - 0.9.1-0.1.beta1
- Port to Python3
