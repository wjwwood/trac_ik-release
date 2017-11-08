Name:           ros-kinetic-trac-ik
Version:        1.4.6
Release:        0%{?dist}
Summary:        ROS trac_ik package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/trac_ik
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-trac-ik-examples
Requires:       ros-kinetic-trac-ik-kinematics-plugin
Requires:       ros-kinetic-trac-ik-lib
BuildRequires:  ros-kinetic-catkin

%description
The ROS packages in this repository were created to provide an improved
alternative Inverse Kinematics solver to the popular inverse Jacobian methods in
KDL. TRAC-IK handles joint-limited chains better than KDL without increasing
solve time.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Nov 08 2017 Patrick Beeson <pbeeson@traclabs.com> - 1.4.6-0
- Autogenerated by Bloom

* Wed Dec 21 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.5-1
- Autogenerated by Bloom

* Wed Dec 21 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.5-0
- Autogenerated by Bloom

