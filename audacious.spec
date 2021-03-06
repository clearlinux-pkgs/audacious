#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : audacious
Version  : 4.0.5
Release  : 4
URL      : https://distfiles.audacious-media-player.org/audacious-4.0.5.tar.bz2
Source0  : https://distfiles.audacious-media-player.org/audacious-4.0.5.tar.bz2
Summary  : Audacious is a versatile and handy multi platform media player
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-SA-4.0
Requires: audacious-bin = %{version}-%{release}
Requires: audacious-data = %{version}-%{release}
Requires: audacious-lib = %{version}-%{release}
Requires: audacious-license = %{version}-%{release}
Requires: audacious-locales = %{version}-%{release}
Requires: audacious-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : pkgconfig(Qt5Core)

%description
These SVG files have been un-optimized to work around the following librsvg bug:
https://bugzilla.gnome.org/show_bug.cgi?id=620923

%package bin
Summary: bin components for the audacious package.
Group: Binaries
Requires: audacious-data = %{version}-%{release}
Requires: audacious-license = %{version}-%{release}

%description bin
bin components for the audacious package.


%package data
Summary: data components for the audacious package.
Group: Data

%description data
data components for the audacious package.


%package dev
Summary: dev components for the audacious package.
Group: Development
Requires: audacious-lib = %{version}-%{release}
Requires: audacious-bin = %{version}-%{release}
Requires: audacious-data = %{version}-%{release}
Provides: audacious-devel = %{version}-%{release}
Requires: audacious = %{version}-%{release}

%description dev
dev components for the audacious package.


%package lib
Summary: lib components for the audacious package.
Group: Libraries
Requires: audacious-data = %{version}-%{release}
Requires: audacious-license = %{version}-%{release}

%description lib
lib components for the audacious package.


%package license
Summary: license components for the audacious package.
Group: Default

%description license
license components for the audacious package.


%package locales
Summary: locales components for the audacious package.
Group: Default

%description locales
locales components for the audacious package.


%package man
Summary: man components for the audacious package.
Group: Default

%description man
man components for the audacious package.


%prep
%setup -q -n audacious-4.0.5
cd %{_builddir}/audacious-4.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604537323
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1604537323
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/audacious
cp %{_builddir}/audacious-4.0.5/COPYING %{buildroot}/usr/share/package-licenses/audacious/e3d02f6d1beceb28df3d3a23405d75c520c7f877
%make_install
%find_lang audacious

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/audacious
/usr/bin/audtool

%files data
%defattr(-,root,root,-)
/usr/share/applications/audacious.desktop
/usr/share/audacious/AUTHORS
/usr/share/audacious/COPYING
/usr/share/icons/hicolor/48x48/apps/audacious.png
/usr/share/icons/hicolor/scalable/apps/audacious.svg

%files dev
%defattr(-,root,root,-)
/usr/include/audacious/audtag.h
/usr/include/libaudcore/audio.h
/usr/include/libaudcore/audstrings.h
/usr/include/libaudcore/drct.h
/usr/include/libaudcore/equalizer.h
/usr/include/libaudcore/export.h
/usr/include/libaudcore/hook.h
/usr/include/libaudcore/i18n.h
/usr/include/libaudcore/index.h
/usr/include/libaudcore/inifile.h
/usr/include/libaudcore/interface.h
/usr/include/libaudcore/list.h
/usr/include/libaudcore/mainloop.h
/usr/include/libaudcore/multihash.h
/usr/include/libaudcore/objects.h
/usr/include/libaudcore/playlist.h
/usr/include/libaudcore/plugin.h
/usr/include/libaudcore/plugins.h
/usr/include/libaudcore/preferences.h
/usr/include/libaudcore/probe.h
/usr/include/libaudcore/ringbuf.h
/usr/include/libaudcore/runtime.h
/usr/include/libaudcore/templates.h
/usr/include/libaudcore/threads.h
/usr/include/libaudcore/tinylock.h
/usr/include/libaudcore/tuple.h
/usr/include/libaudcore/vfs.h
/usr/include/libaudcore/vfs_async.h
/usr/include/libaudcore/visualizer.h
/usr/include/libaudqt/colorbutton.h
/usr/include/libaudqt/export.h
/usr/include/libaudqt/iface.h
/usr/include/libaudqt/info-widget.h
/usr/include/libaudqt/libaudqt.h
/usr/include/libaudqt/menu.h
/usr/include/libaudqt/treeview.h
/usr/lib64/libaudcore.so
/usr/lib64/libaudqt.so
/usr/lib64/libaudtag.so
/usr/lib64/pkgconfig/audacious.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaudcore.so.5
/usr/lib64/libaudcore.so.5.2.0
/usr/lib64/libaudqt.so.2
/usr/lib64/libaudqt.so.2.2.0
/usr/lib64/libaudtag.so.3
/usr/lib64/libaudtag.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/audacious/e3d02f6d1beceb28df3d3a23405d75c520c7f877

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/audacious.1
/usr/share/man/man1/audtool.1

%files locales -f audacious.lang
%defattr(-,root,root,-)

