#
# spec file for package intltool
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           intltool
Version:        0.50.2
Release:        0
License:        GPL-2.0+
Summary:        Internationalization Tool Collection
Url:            https://edge.launchpad.net/intltool/
Group:          Development/Tools/Other
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  perl-XML-Parser
Requires:       gettext-tools
Requires:       perl-XML-Parser
Provides:       xml-i18n-tools
Obsoletes:      xml-i18n-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Some scripts to support translators working on GNOME and similar
programs. Data available in XML files (.oaf, .desktop, .sheet, and
more) can be extracted into PO files. After translation, the new
information is written back into the XML files.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
%make_install

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%defattr(-, root, root)
%{_bindir}/intltool-*
%{_bindir}/intltoolize
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/intltool.m4
%{_datadir}/%{name}/
%doc %{_mandir}/man8/intltool-*.8%{?ext_man}
%doc %{_mandir}/man8/intltoolize.8%{?ext_man}

%changelog
