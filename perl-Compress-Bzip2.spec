#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Compress-Bzip2
Version  : 2.26
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Compress-Bzip2-2.26.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Compress-Bzip2-2.26.tar.gz
Summary  : 'Interface to Bzip2 compression library'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0 bzip2-1.0.6
Requires: perl-Compress-Bzip2-lib = %{version}-%{release}
Requires: perl-Compress-Bzip2-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : bzip2-dev

%description
The files here are from the bzip2 1.0.6 distribution, unaltered,
from http://sources.redhat.com/bzip2, by Julian Seward, jseward@acm.org

%package dev
Summary: dev components for the perl-Compress-Bzip2 package.
Group: Development
Requires: perl-Compress-Bzip2-lib = %{version}-%{release}
Provides: perl-Compress-Bzip2-devel = %{version}-%{release}

%description dev
dev components for the perl-Compress-Bzip2 package.


%package lib
Summary: lib components for the perl-Compress-Bzip2 package.
Group: Libraries
Requires: perl-Compress-Bzip2-license = %{version}-%{release}

%description lib
lib components for the perl-Compress-Bzip2 package.


%package license
Summary: license components for the perl-Compress-Bzip2 package.
Group: Default

%description license
license components for the perl-Compress-Bzip2 package.


%prep
%setup -q -n Compress-Bzip2-2.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Compress-Bzip2
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Compress-Bzip2/COPYING
cp bzlib-src/LICENSE %{buildroot}/usr/share/package-licenses/perl-Compress-Bzip2/bzlib-src_LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Compress/Bzip2.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Compress/Bzip2/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Compress::Bzip2.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Compress/Bzip2/Bzip2.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Compress-Bzip2/COPYING
/usr/share/package-licenses/perl-Compress-Bzip2/bzlib-src_LICENSE
