# http://github.com/golang/mock

%global goipath         github.com/golang/mock
%global commit          58cd061d09382b6011f84c1291ebe50ef2e25bab
%global goreqflags      -t mockgen/tests
# Run tests in check section
%bcond_without check

%gometa

Name:           golang-googlecode-gomock
Version:        0
Release:        0.15%{?dist}
Summary:        Mocking framework for the Go
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
GoMock is a mocking framework for the [Go programming language][golang].
It integrates well with Go's built-in `testing` package,
but can be used in other contexts too.

%package -n %{goname}-devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/net/context)

Obsoletes:     golang-github-golang-mock-devel

%description -n %{goname}-devel
GoMock is a mocking framework for the [Go programming language][golang].
It integrates well with Go's built-in `testing` package,
but can be used in other contexts too.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup

%build
%gobuildroot
%gobuild -o _bin/mockgen %{goipath}/mockgen

%install
%goinstall
install -Dpm 0755 _bin/mockgen %{buildroot}%{_bindir}/mockgen

%if %{with check}
%check
%gochecks
%endif

%files
%license LICENSE
%{_bindir}/mockgen

%files -n %{goname}-devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS CONTRIBUTORS

%changelog
* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0-0.15
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git58cd061
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git58cd061
- Rename the package back to golang-github-golang-mock-devel

* Mon Mar 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git58cd061
- Bump to 58cd061d09382b6011f84c1291ebe50ef2e25bab
  Update to new Go guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitd581abf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitd581abf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitd581abf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitd581abf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitd581abf
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitd581abf
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitd581abf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitd581abf
- Choose the correct devel subpackage
  related: #1250520

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitd581abf
- Update spec file to spec-2.0
  resolves: #1250520

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.hge033c7513ca3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.hge033c7513ca3
- First package for Fedora
