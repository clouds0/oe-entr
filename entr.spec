Name:           entr
Version:        4.5
Release:        1%{?dist}
Summary:        Run arbitrary commands when files change

License:        ISC
URL:            http://eradman.com/%{name}project/
Source0:        http://eradman.com/%{name}project/code/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
A file watcher, which can run specified commands
when target files change.

%global debug_package %{nil}

%prep
%setup -q

%build
./configure
make

%install
%make_install
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp LICENSE %{buildroot}/%{_docdir}/%{name}/
cp README.md %{buildroot}/%{_docdir}/%{name}/
cp NEWS %{buildroot}/%{_docdir}/%{name}


%check
make test

%files
/usr/local/bin/entr
/usr/local/share/man/man1/entr.1
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/LICENSE
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README.md


%changelog
* Tue Jun 4 2020 Leo <leechau@126.com> - 4.5-1
- entr v4.5 package

