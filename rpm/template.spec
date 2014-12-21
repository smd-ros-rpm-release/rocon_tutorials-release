Name:           ros-indigo-rocon-app-manager-tutorials
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS rocon_app_manager_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rocon_app_manager_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rocon-app-manager
Requires:       ros-indigo-rocon-apps
Requires:       ros-indigo-rocon-interactions
Requires:       ros-indigo-rocon-master-info
Requires:       ros-indigo-rocon-qt-listener
Requires:       ros-indigo-rocon-remocon
Requires:       ros-indigo-turtle-concert
Requires:       ros-indigo-turtlesim
BuildRequires:  ros-indigo-catkin

%description
Tutorials for the rocon app manager.

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
* Sun Dec 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.2-0
- Autogenerated by Bloom

