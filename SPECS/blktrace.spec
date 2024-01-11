Summary: Utilities for performing block layer IO tracing in the Linux kernel
Name: blktrace
Version: 1.2.0
Release: 10%{?dist}
License: GPLv2+
Group: Development/System
Source:  http://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2
Url: http://brick.kernel.dk/snaps

BuildRequires: python3-devel
BuildRequires: gcc, libaio-devel, librsvg2-devel

Patch0: blktrace-fix-btt-overflow.patch
Patch1: blktrace-python3.patch

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space.  This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

You should install the blktrace package if you need to gather detailed
information about IO patterns.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -i '1s=^#!/usr/bin/python3=#!%{__python3}=' \
    btt/{btt_plot.py,bno_plot.py}

%build
make CFLAGS="%{optflags} %{build_ldflags}" all

%install
rm -rf %{buildroot}
make dest=%{buildroot} prefix=%{buildroot}/%{_prefix} mandir=%{buildroot}/%{_mandir} install

%files
%doc README COPYING
%{_bindir}/blkparse
%{_bindir}/blkrawverify
%{_bindir}/bno_plot.py
%{_bindir}/btt
%{_bindir}/verify_blkparse
%{_bindir}/blkiomon
%{_bindir}/blktrace
%{_bindir}/btrace
%{_bindir}/btrecord
%{_bindir}/btreplay
%{_mandir}/man1/blkparse.*
%{_mandir}/man1/blkrawverify.*
%{_mandir}/man1/bno_plot.*
%{_mandir}/man1/btt.*
%{_mandir}/man1/verify_blkparse.*
%{_mandir}/man8/blkiomon.*
%{_mandir}/man8/blktrace.*
%{_mandir}/man8/btrace.*
%{_mandir}/man8/btrecord.*
%{_mandir}/man8/btreplay.*

%package -n iowatcher
Summary: Utility for visualizing block layer IO patterns and performance
Requires: blktrace sysstat theora-tools librsvg2-tools

%description -n iowatcher
iowatcher generates graphs from blktrace runs to help visualize IO patterns and
performance as SVG images or movies. It can plot multiple blktrace runs
together, making it easy to compare the differences between different benchmark
runs.

You should install the iowatcher package if you need to visualize detailed
information about IO patterns.

%files -n iowatcher
%doc README iowatcher/COPYING
%{_bindir}/iowatcher
%{_mandir}/man1/iowatcher.*

%changelog
* Tue May 14 2019 Eric Sandeen <sandeen@redhat.com> - 1.2.0-10
- Add librsvg2-tools dependency to iowatcher (#1700065)

* Wed Jun 20 2018 Tomas Orsava <torsava@redhat.com> - 1.2.0-9
- Switch hardcoded python3 shebangs into the %%{__python3} macro
- Add missing BuildRequires on python3-devel so that %%{__python3} macro is
  defined

* Thu May 24 2018 Eric Sandeen <sandeen@redhat.com> - 1.2.0-8
- Fix CVE-2018-10689 buffer overflow (#1575121)

* Wed May 16 2018 Eric Sandeen <sandeen@redhat.com> - 1.2.0-7
- Make scripts python3-ready

* Mon May 07 2018 Eric Sandeen <sandeen@redhat.com> - 1.2.0-6
- Fix for CVE-2018-10689 (#1575120)

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> - 1.2.0-5
- BuildRequires: gcc

* Sun Feb 25 2018 Florian Weimer <fweimer@redhat.com> - 1.2.0-4
- Use LDFLAGS from redhat-rpm-config

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Nov 06 2017 Eric Sandeen <sandeen@redhat.com> - 1.2.0-1
- New upstream version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 26 2014 Andrew Price <anprice@redhat.com> - 1.1.0-1
- New upstream version
- Add iowatcher subpackage
- Remove obsolete 'clean' and 'defattr' sections

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 Eric Sandeen <sandeen@redhat.com> - 1.0.5-4
- Remove tex->pdf doc build, fix build & lighten up buildreqs

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 23 2012 Eric Sandeen <sandeen@redhat.com> - 1.0.5-1
- New upstream version

* Tue Jan 31 2012 Eric Sandeen <sandeen@redhat.com> - 1.0.4-1
- New upstream version

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Eric Sandeen <sandeen@redhat.com> - 1.0.3-1
- New upstream version

* Wed Mar 16 2011 Eric Sandeen <sandeen@redhat.com> - 1.0.2-1
- New upstream version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Eric Sandeen <sandeen@redhat.com> - 1.0.1-4
- Fix linking with libpthread (#564775)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-2
- Upstream respun the release tarball to re-include top-level dir
- drop exclude of bno_plot.py[co], not getting built now?

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-1
- New upstream version

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.0-2
- Build PDF documentation after all

* Sun Nov 02 2008 Eric Sandeen <sandeen@redhat.com> - 1.0.0-1
- New upstream version (now with actual versioning!)

* Fri Feb 08 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.9.20080103162505git
- gcc-4.3 rebuild

* Sat Jan 26 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.8.20080103162505git
- New upstream version

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.6.20071010202719git
- Add libaio-devel to BuildRequires

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.5.20071010202719git
- New upstream version

* Wed Aug 15 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.4.20070730162628git
- Fix up btt/Makefile to accept rpm's CFLAGS

* Tue Aug 14 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.3.20070730162628git
- Just drop the pdf build, bloats the buildroot for such a simple tool

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.2.20070730162628git
- Add ghostscript to BuildRequires, use attr macro for man pages

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.1.20070730162628git
- New package, initial build.
