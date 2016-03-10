Name:           ros-jade-std-srvs
Version:        1.11.2
Release:        0%{?dist}
Summary:        ROS std_srvs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/std_srvs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-message-runtime
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation

%description
Common service definitions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Mar 10 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.2-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.1-0
- Autogenerated by Bloom

* Fri Feb 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.0-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.10.3-0
- Autogenerated by Bloom

