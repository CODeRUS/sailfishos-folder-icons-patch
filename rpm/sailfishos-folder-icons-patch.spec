# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-folder-icons-patch

# >> macros
BuildArch: noarch
# << macros

Summary:    Homescreen icons folder patch
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   lipstick-jolla-home-qt5 >= 0.21.2.5

%description
A homescreen patch that provides icons in folder


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-folder-icons-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-folder-icons-patch
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-folder-icons-patch
# >> files
# << files
