#
# spec file for package yast2-seat-manager
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           yast2-seat-manager
Version:        0.0.1
Release:        0
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-seat-manager.tar.bz2

Requires:       ruby >= 2.0
Requires:       yast2 >= 2.24.1
Requires:       yast2-ruby-bindings >= 1.2.0

BuildRequires:  ruby
BuildRequires:  rubygem-mocha
BuildRequires:  update-desktop-files
BuildRequires:  yast2 >= 2.24.1
BuildRequires:  yast2-ruby-bindings >= 1.2.0

Summary:        YaST2 - Services Manager
License:        GPL-2.0
Group:          System/YaST

Url:            https://github.com/StefanBruens/yast-seat-manager

%description
Provides user interface and libraries to assign mouse, keyboard, display devices and more
individual seats in a multiseat environment.

%prep
%setup -n yast2-seat-manager

%build

%install
rake install DESTDIR="%{buildroot}"
%suse_update_desktop_file seat-manager

%files
%defattr(-,root,root)
# %{_prefix}/share/YaST2/clients/*.rb
# %{_prefix}/share/YaST2/modules/*.rb
%{_prefix}/share/applications/YaST2/seat-manager.desktop
# %{_prefix}/share/YaST2/schema/autoyast/rnc/*.rnc
%doc %dir %{_prefix}/share/doc/packages/yast2-seat-manager/
%doc %{_prefix}/share/doc/packages/yast2-seat-manager/README
%doc %{_prefix}/share/doc/packages/yast2-seat-manager/COPYING

%files doc

%changelog
