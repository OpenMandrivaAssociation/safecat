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
