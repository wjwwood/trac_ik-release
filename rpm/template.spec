Name:           ros-indigo-trac-ik-lib
Version:        1.4.5
Release:        0%{?dist}
Summary:        ROS trac_ik_lib package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       NLopt
Requires:       NLopt-devel
Requires:       boost-devel
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-urdf
BuildRequires:  NLopt-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-kdl-parser
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-urdf

%description
TRAC-IK is a faster, significantly more reliable drop-in replacement for KDL's
pseudoinverse Jacobian solver. The TRAC-IK library has a very similar API to
KDL's IK solver calls, except that the user passes a maximum time instead of a
maximum number of search iterations. Additionally, TRAC-IK allows for error
tolerances to be set independently for each Cartesian dimension
(x,y,z,roll,pitch.yaw).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Dec 21 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.5-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.3-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Patrick Beeson <pbeeson@traclabs.com> - 1.4.2-0
- Autogenerated by Bloom

