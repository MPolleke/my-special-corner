Name: x11-util-macros
BuildArch: noarch
Summary: Macro used for X.org development
Version: 1.19.2
Release: 4
Group: Development/X11
License: MIT
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2

%description
Macros used for X.org development

%prep
%setup -q -n util-macros-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%dir %{_datadir}/util-macros
%{_datadir}/util-macros/INSTALL
%{_datadir}/aclocal/xorg-macros.m4
%{_datadir}/pkgconfig/xorg-macros.pc




%changelog
* Mon Mar 21 2022 umeabot <umeabot> 1.19.2-4.mga9
+ Revision: 1810783
- Mageia 9 Mass Rebuild
+ danf <danf>
- Switch URLs from http: to https:

* Wed Feb 12 2020 umeabot <umeabot> 1.19.2-3.mga8
+ Revision: 1508266
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x

* Fri Sep 21 2018 umeabot <umeabot> 1.19.2-2.mga7
+ Revision: 1292155
- Mageia 7 Mass Rebuild

* Fri Mar 09 2018 tv <tv> 1.19.2-1.mga7
+ Revision: 1207523
- new release

* Sat Nov 04 2017 tv <tv> 1.19.1-1.mga7
+ Revision: 1175782
- new release

* Mon Feb 08 2016 umeabot <umeabot> 1.19.0-5.mga6
+ Revision: 950467
- Mageia 6 Mass Rebuild

* Fri Oct 31 2014 cjw <cjw> 1.19.0-4.mga5
+ Revision: 795072
- add /usr/share/util-macros to file list

* Wed Oct 15 2014 umeabot <umeabot> 1.19.0-3.mga5
+ Revision: 748069
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 1.19.0-2.mga5
+ Revision: 690527
- Mageia 5 Mass Rebuild

* Tue Apr 01 2014 tv <tv> 1.19.0-1.mga5
+ Revision: 611053
- new release

* Tue Feb 04 2014 tv <tv> 1.18.0-1.mga5
+ Revision: 581788
- rebuild for new perl

* Sat Oct 19 2013 umeabot <umeabot> 1.17.1-3.mga4
+ Revision: 534481
- Mageia 4 Mass Rebuild

* Thu Sep 12 2013 tv <tv> 1.17.1-2.mga4
+ Revision: 477905
- new release

* Mon Jan 14 2013 umeabot <umeabot> 1.17-2.mga3
+ Revision: 386398
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Tue May 29 2012 tv <tv> 1.17-1.mga3
+ Revision: 249366
- new release

* Fri Mar 09 2012 tv <tv> 1.16.2-1.mga2
+ Revision: 222232
- new release

* Sun Jan 22 2012 tv <tv> 1.16.1-1.mga2
+ Revision: 199610
- new release

* Thu Dec 08 2011 tv <tv> 1.16.0-1.mga2
+ Revision: 179142
- new release

* Wed Jun 29 2011 tv <tv> 1.15.0-1.mga2
+ Revision: 116149
- new release

* Thu Jun 16 2011 tv <tv> 1.14.0-1.mga2
+ Revision: 108449
- new release

* Fri Apr 01 2011 tv <tv> 1.13.0-1.mga1
+ Revision: 79626
- new release

* Tue Mar 01 2011 tv <tv> 1.12.0-1.mga1
+ Revision: 62140
- use %%configure2_5x
- remove useless "echo"
- use %%makeinstall_std
- new release

* Sat Jan 08 2011 blino <blino> 1.11.0-1.mga1
+ Revision: 920
- imported package x11-util-macros


* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.11.0-1mdv2011.0
+ Revision: 590412
- new release

* Fri Sep 24 2010 Thierry Vignaud <tv@mandriva.org> 1.10.1-1mdv2011.0
+ Revision: 580845
- new release

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 556419
- new release

* Mon Apr 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.7.0-1mdv2010.1
+ Revision: 531620
- New version: 1.7.0

* Fri Mar 12 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.6.1-1mdv2010.1
+ Revision: 518393
- New version: 1.6.1

* Fri Feb 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.6.0-1mdv2010.1
+ Revision: 501250
- New version: 1.6.0

* Mon Jan 18 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5.0-1mdv2010.1
+ Revision: 493193
- New version: 1.5.0

* Mon Jan 18 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.4.2-1mdv2010.1
+ Revision: 493080
- New version: 1.4.2

* Tue Dec 15 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.4.1-1mdv2010.1
+ Revision: 478932
- New version: 1.4.1

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3.0-1mdv2010.1
+ Revision: 463695
- New version: 1.3.0

* Fri Jun 19 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.2-1mdv2010.0
+ Revision: 387309
- update to version 1.2.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 321322
- New version: 1.2.1

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.1.6-2mdv2009.0
+ Revision: 266066
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.6-1mdv2009.0
+ Revision: 192829
- Update to version 1.1.6.

* Wed Feb 13 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.5-5mdv2008.1
+ Revision: 167173
- Revert to use upstream tarball, build requires and remove non mandatory patches.

* Wed Dec 26 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.1.5-4mdv2008.1
+ Revision: 137948
- Properly use tag util-macros-1.1.5 to generate tarball, and update to
  generate patches from that point.
- Fix documentation comment in spec file.
- Update x11-util-macros, required/used by all modules

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.5-3mdv2008.1
+ Revision: 98601
- spec cleanup (fix description and packager tags)


* Sun Feb 18 2007 Götz Waschk <waschk@mandriva.org> 1.1.5-2mdv2007.0
+ Revision: 122427
- rebuild just for fun

* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.1.5-1mdv2007.1
+ Revision: 116434
- new upstream version: 1.1.5

* Wed Aug 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.1.1-1mdv2007.0
+ Revision: 58706
- new upstream release (1.1.1):
  * Remove man suffix special-casing for GNU userland systems

* Thu Aug 03 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.1.0-1mdv2007.0
+ Revision: 42989
- new upstream release (1.1.0):
  * Adds 3 new autoconf macros:
- XORG_MACROS_VERSION - check to make sure configure is generated with a
  new enough version of util-macros when using macros added after 1.0.0
- XORG_WITH_LINT - defines --with-lint for checking source code with tools
  such as lint & sparse (disabled by default)
- XORG_LINT_LIBRARY - defines --enable-lint-library for making lint
  library to check programs against which link with a library (disabled by
  default)
  * Also updates the XORG_MANPAGE_SECTIONS macro to make GNU/kFreeBSD man page
  sections match the Linux man page sections.
- rebuild to fix cooker uploading
- X11R7.1
- adding the %%clean section
- Fixed packager tag
- increment release
- Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

