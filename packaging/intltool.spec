Name:           intltool
Version:        0.50.2
Release:        0
License:        GPL-2.0+
Summary:        Internationalization Tool Collection
Url:            https://edge.launchpad.net/intltool/
Group:          Development/Tools
Source:         %{name}-%{version}.tar.gz
Source1001: 	intltool.manifest
BuildRequires:  perl-XML-Parser
Requires:       gettext-tools
Requires:       perl-XML-Parser
Provides:       xml-i18n-tools
Obsoletes:      xml-i18n-tools
BuildArch:      noarch
Requires:       perl-XML-Parser

%description
Some scripts to support translators working on GNOME and similar
programs. Data available in XML files (.oaf, .desktop, .sheet, and
more) can be extracted into PO files. After translation, the new
information is written back into the XML files.

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
%configure
make %{?_smp_mflags}

%check
make check

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%defattr(-, root, root)
%{_bindir}/intltool-*
%{_bindir}/intltoolize
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/intltool.m4
%{_datadir}/%{name}/
%doc %{_mandir}/man8/intltool-*.8%{?ext_man}
%doc %{_mandir}/man8/intltoolize.8%{?ext_man}

%changelog
