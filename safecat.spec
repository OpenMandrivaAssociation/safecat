%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Secure File Wiping and Deletion
Name:		safecat
Version:	1.13
Release:	%mkrel 4
License:	BSD
Group:		File tools
URL:		http://jeenyus.net/~budney/linux/software/safecat.html
Source0:	http://jeenyus.net/~budney/linux/software/safecat/%{name}-%{version}.tar.bz2
Source1:	README.MDK
BuildRequires:	dietlibc-devel >= 0.20
BuildRequires:  groff-for-man
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
safecat is an implementation of D. J. Bernstein's maildir algorithm. It can be
used to write mail messages to a qmail-style maildir, or to write data to a
"spool" directory reliably. There are no lockfiles with safecat, and nothing is
left to chance. If safecat returns a successful exit status, then you can be
(practically) 100% sure your data is safely committed to disk. Further, if data
is written to a directory using safecat (or other implementations of the
maildir algorithm), then every file in that directory is guaranteed to be
complete. If safecat fails to write all of the data, there will be no file at
all in the destination directory.

Of course, you know that such a thing cannot be: between UNIX and the different
hardware options available, a 100% guarantee is not possible. However, safecat
takes every precaution possible in writing your data.

%prep

%setup -q
cp %{SOURCE1} README.MDK

%build
echo "diet gcc -Os -pipe -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE" > conf-cc
echo "diet gcc -Os -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -static -s" > conf-ld
echo "%{_prefix}" > conf-root
make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 safecat %{buildroot}%{_bindir}/
install -m0755 maildir %{buildroot}%{_bindir}/
install -m0644 safecat.1 %{buildroot}%{_mandir}/man1/
install -m0644 maildir.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc COPYING CHANGES INSTALL README README.MDK
%{_bindir}/safecat
%{_bindir}/maildir
%{_mandir}/man1/safecat.1*
%{_mandir}/man1/maildir.1*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.13-4mdv2010.0
+ Revision: 433600
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.13-3mdv2009.0
+ Revision: 269239
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1.13-2mdv2009.0
+ Revision: 217545
- rebuilt against dietlibc-devel-0.32

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.13-1mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.13-1mdv2007.0
+ Revision: 113789
- Import safecat

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.13-1mdv2007.1
- 1.13

* Sun Dec 25 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.12-3mdk
- Fix BuildRequires
- use mkrel

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.12-2mdk
- rebuild

* Thu Nov 04 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.12-1mdk
- initial mandrake package

