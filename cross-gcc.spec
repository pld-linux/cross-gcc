#
# Conditional build:
%bcond_without	cloog 		# cloog
# Targets:
%bcond_without	aarch64			# enable aarch64
%bcond_without	alpha			# enable alpha
%bcond_without	arm			# enable arm
%bcond_without	avr32			# enable avr32
%bcond_without	blackfin		# enable blackfin
%bcond_without	c6x			# enable c6x
%bcond_without	cris			# enable cris
%bcond_without	frv			# enable frv
%bcond_without	h8300			# enable h8300
%bcond_without	hppa			# enable hppa
%bcond_without	hppa64			# enable hppa64
%bcond_without	ia64			# enable ia64
%bcond_without	m32r			# enable m32r
%bcond_without	m68k			# enable m68k
%bcond_without	microblaze		# enable microblaze
%bcond_without	mips64			# enable mips64
%bcond_without	mn10300			# enable mn10300
%bcond_without	nios2			# enable nios2
%bcond_without	powerpc64		# enable powerpc64
%bcond_without	s390x			# enable s390x
%bcond_without	sh			# enable sh
%bcond_without	sh64			# enable sh64
%bcond_without	sparc64			# enable sparc64
%bcond_without	tile			# enable tile
%bcond_without	x86_64			# enable x86_64
%bcond_without	xtensa			# enable xtensa

# built compiler generates lots of ICEs
# - none at this time

# gcc considers obsolete
%undefine with_score

# gcc doesn't build
# - sh64 doesn't build on pld:
# ../../gcc-4.9.2-20141212/gcc/genmultilib[264]: shift: nothing to shift
# Makefile:1851: recipe for target 's-mlib' failed
%undefine with_sh64
# packaging error, files packaged to gcc-hppa-linux-gnu and gcc-hppa64-linux-gnu
%undefine with_hppa64

# 32-bit packages we don't build as we can use the 64-bit package instead
%undefine with_i386
%undefine with_mips
%undefine with_powerpc
%undefine with_s390
%undefine with_sh4
%undefine with_sparc

# gcc doesn't support
%undefine with_metag
%undefine with_openrisc

# not available in binutils-2.22
%undefine with_unicore32

%define	multilib_64_archs sparc64 ppc64 s390x x86_64

# we won't build libgcc for these as it depends on C library or kernel headers
%define no_libgcc_targets	nios2*|tile-*

###############################################################################
#
# The gcc versioning information.  In a sed command below, the specfile winds
# pre-release version numbers in BASE-VER back to the last actually-released
# number.
%define	DATE 20141212
%define	SVNREV 218667

%define srcdir gcc-%{version}-%{DATE}
%define	cross_binutils_version 2.24
%define	isl_version 0.12.2
%define cloog_version 0.18.1

Summary:	Cross C compiler
Name:		cross-gcc
Version:	4.9.2
Release:	0.1
# libgcc, libgfortran, libmudflap, libgomp, libstdc++ and crtstuff have GCC Runtime Exception.
License:	GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group:		Development/Languages
URL:		http://gcc.gnu.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-4_7-branch@%{SVNREV} gcc-%{version}-%{DATE}
# tar cf - gcc-%{version}-%{DATE} | bzip2 -9 > gcc-%{version}-%{DATE}.tar.bz2
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/cross-gcc/%{srcdir}.tar.bz2/ccd8cac944582f8d2ddf5274a15df176/%{srcdir}.tar.bz2
# Source0-md5:	ccd8cac944582f8d2ddf5274a15df176
Source1:	ftp://gcc.gnu.org/pub/gcc/infrastructure/isl-%{isl_version}.tar.bz2
# Source1-md5:	e039bfcfb6c2ab039b8ee69bf883e824
Source2:	ftp://gcc.gnu.org/pub/gcc/infrastructure/cloog-%{cloog_version}.tar.gz
# Source2-md5:	e34fca0540d840e5d0f6427e98c92252
Patch0:		gcc49-hack.patch
Patch1:		gcc49-java-nomulti.patch
Patch2:		gcc49-ppc32-retaddr.patch
Patch3:		gcc49-rh330771.patch
Patch4:		gcc49-i386-libgomp.patch
Patch5:		gcc49-sparc-config-detection.patch
Patch6:		gcc49-libgomp-omp_h-multilib.patch
Patch7:		gcc49-libtool-no-rpath.patch
Patch8:		gcc49-cloog-dl.patch
Patch9:		gcc49-cloog-dl2.patch
Patch10:	gcc49-pr38757.patch
Patch11:	gcc49-libstdc++-docs.patch
Patch12:	gcc49-no-add-needed.patch
Patch13:	gcc49-color-auto.patch
Patch14:	gcc49-libgo-p224.patch
Patch15:	gcc49-aarch64-async-unw-tables.patch
Patch16:	gcc49-aarch64-unwind-opt.patch
Patch17:	gcc49-pr64269.patch
Patch900:	cross-intl-filename.patch
# ia64 - http://gcc.gnu.org/bugzilla/show_bug.cgi?id=44553
# m68k - http://gcc.gnu.org/bugzilla/show_bug.cgi?id=53557
# alpha - http://gcc.gnu.org/bugzilla/show_bug.cgi?id=55344
Patch901:	cross-gcc-with-libgcc.patch
Patch903:	cross-gcc-bfin.patch
Patch904:	cross-gcc-c6x.patch
Patch1100:	cloog-0.18.1-ppc64le-config.patch
BuildRequires:	cross-binutils-common >= %{cross_binutils_version}
BuildRequires:	binutils >= 2.20.51.0.2-12
BuildRequires:	bison
BuildRequires:	dejagnu
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	sharutils
BuildRequires:	texinfo
BuildRequires:	zlib-devel
# make sure pthread.h doesn't contain __thread tokens
# make sure glibc supports stack protector
# make sure glibc supports DT_GNU_HASH
BuildRequires:	elfutils-devel >= 0.147
BuildRequires:	glibc-devel >= 2.4.90-13
BuildRequires:	gmp-devel >= 4.2
BuildRequires:	libmpc-devel >= 0.8.1
BuildRequires:	mpfr-devel >= 2.3.1
Provides:	bundled(libiberty)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define builddir %{_builddir}/%{name}-%{version}

%description
Cross-build GNU C compiler collection.

%package common
Summary:	Cross-build GNU C compiler documentation and translation files
Group:		Development/Languages
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description common
Documentation, manual pages and translation files for cross-build GNU
C compiler.

This is the common part of a set of cross-build GNU C compiler
packages for building kernels for other architectures. No support for
cross-building user space programs is currently supplied as that would
massively multiply the number of packages.

%define do_package() \
%if %{expand:%%{?with_%{2}:1}%%{!?with_%{2}:0}} \
%package -n gcc-%1 \
Summary:	Cross-build binary utilities for %1 \
Group:		Development/Languages \
BuildRequires:	binutils-%1 >= %{cross_binutils_version}\
Requires:	%{name}-common = %{version}-%{release}\
Requires:	binutils-%1 >= %{cross_binutils_version}\
\
%description -n gcc-%1 \
Cross-build GNU C compiler. \
\
Only building kernels is currently supported. Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
\
%package -n gcc-c++-%1 \
Summary:	Cross-build binary utilities for %1 \
Group:		Development/Languages \
Requires:	gcc-%1 = %{version}-%{release}\
\
%description -n gcc-c++-%1 \
Cross-build GNU C++ compiler. \
\
Only the compiler is provided; not libstdc++. Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
%endif

%define do_symlink() \
%if %{expand:%%{?with_%{2}:1}%%{!?with_%{2}:0}} \
%package -n gcc-%1 \
Summary:	Cross-build binary utilities for %1 \
Group:		Development/Languages \
Requires:	gcc-%3 = %{version}-%{release}\
\
%description -n gcc-%1 \
Cross-build GNU C++ compiler. \
\
Only building kernels is currently supported. Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
\
%package -n gcc-c++-%1 \
Summary:	Cross-build binary utilities for %1 \
Group:		Development/Languages \
Requires:	gcc-%1 = %{version}-%{release}\
Requires:	gcc-c++-%3 = %{version}-%{release}\
\
%description -n gcc-c++-%1 \
Cross-build GNU C++ compiler. \
\
Only the compiler is provided; not libstdc++. Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
%endif

%do_package alpha-linux-gnu	alpha
%do_package arm-linux-gnu	arm
%do_package aarch64-linux-gnu	aarch64
%do_package avr32-linux-gnu	avr32
%do_package bfin-linux-gnu	blackfin
%do_package c6x-linux-gnu	c6x
%do_package cris-linux-gnu	cris
%do_package frv-linux-gnu	frv
%do_package h8300-linux-gnu	h8300
%do_package hppa-linux-gnu	hppa
%do_package hppa64-linux-gnu	hppa64
%do_package i386-linux-gnu	i386
%do_package ia64-linux-gnu	ia64
%do_package m32r-linux-gnu	m32r
%do_package m68k-linux-gnu	m68k
%do_package metag-linux-gnu	metag
%do_package microblaze-linux-gnu microblaze
%do_package mips-linux-gnu	mips
%do_package mips64-linux-gnu	mips64
%do_package mn10300-linux-gnu	mn10300
%do_package nios2-linux-gnu	nios2
%do_package openrisc-linux-gnu	openrisc
%do_package powerpc-linux-gnu	powerpc
%do_package powerpc64-linux-gnu	powerpc64
%do_symlink ppc-linux-gnu	powerpc	powerpc-linux-gnu
%do_symlink ppc64-linux-gnu	powerpc64	powerpc64-linux-gnu
%do_package s390-linux-gnu	s390
%do_package s390x-linux-gnu	s390x
%do_package score-linux-gnu	score
%do_package sh-linux-gnu	sh
%do_package sh4-linux-gnu	sh4
%do_package sh64-linux-gnu	sh64
%do_package sparc-linux-gnu	sparc
%do_package sparc64-linux-gnu	sparc64
%do_package tile-linux-gnu	tile
%do_package unicore32-linux-gnu	unicore32
%do_package x86_64-linux-gnu	x86_64
%do_package xtensa-linux-gnu	xtensa

%prep
%setup -qc -a 1 -a 2
cd %{srcdir}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%if %{with cloog}
%patch8 -p0
%patch9 -p0
%endif
%patch10 -p0
# % if %{with libstdcxx_docs}
# % patch11 -p0
# % endif
%patch12 -p0
%patch13 -p0
%patch14 -p0
rm -f libgo/go/crypto/elliptic/p224{,_test}.go
%patch15 -p0
%patch16 -p0
%patch17 -p0

%patch900 -p0
%patch901 -p1
%patch903 -p0
%patch904 -p0

cd ..
%patch1100 -p0
cd %{srcdir}

# Move the version number back
sed -i -e 's/4\.9\.3/4.9.2/' gcc/BASE-VER
echo 'PLD-Linux Cross %{version}-%{release}' > gcc/DEV-PHASE

# Default to -gdwarf-4 -fno-debug-types-section rather than -gdwarf-2
sed -i '/UInteger Var(dwarf_version)/s/Init(2)/Init(4)/' gcc/common.opt
sed -i '/flag_debug_types_section/s/Init(1)/Init(0)/' gcc/common.opt
sed -i '/dwarf_record_gcc_switches/s/Init(0)/Init(1)/' gcc/common.opt
sed -i 's/\(may be either 2, 3 or 4; the default version is \)2\./\14./' gcc/doc/invoke.texi

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

cat > target.list <<EOF
%{?with_alpha:alpha-linux-gnu}
%{?with_arm:arm-linux-gnu}
%{?with_aarch64:aarch64-linux-gnu}
%{?with_avr32:avr32-linux-gnu}
%{?with_blackfin:bfin-linux-gnu}
%{?with_c6x:c6x-linux-gnu}
%{?with_cris:cris-linux-gnu}
%{?with_frv:frv-linux-gnu}
%{?with_h8300:h8300-linux-gnu}
%{?with_hppa:hppa-linux-gnu}
%{?with_hppa64:hppa64-linux-gnu}
%{?with_i386:i386-linux-gnu}
%{?with_ia64:ia64-linux-gnu}
%{?with_m32r:m32r-linux-gnu}
%{?with_m68k:m68k-linux-gnu}
%{?with_metag:metag-linux-gnu}
%{?with_microblaze:microblaze-linux-gnu}
%{?with_mips:mips-linux-gnu}
%{?with_mips64:mips64-linux-gnu}
%{?with_mn10300:mn10300-linux-gnu}
%{?with_nios2:nios2-linux-gnu}
%{?with_openrisc:openrisc-linux-gnu}
%{?with_powerpc:powerpc-linux-gnu}
%{?with_powerpc64:powerpc64-linux-gnu}
%{?with_s390:s390-linux-gnu}
%{?with_s390x:s390x-linux-gnu}
%{?with_score:score-linux-gnu}
%{?with_sh:sh-linux-gnu}
%{?with_sh4:sh4-linux-gnu}
%{?with_sh64:sh64-linux-gnu}
%{?with_sparc:sparc-linux-gnu}
%{?with_sparc64:sparc64-linux-gnu}
%{?with_tile:tile-linux-gnu}
%{?with_unicore32:unicore32-linux-gnu}
%{?with_x86_64:x86_64-linux-gnu}
%{?with_xtensa:xtensa-linux-gnu}
EOF

if [ $(wc -w < target.list) = 0 ]; then
	echo >&2 "No targets selected"
	exit 8
fi

%build

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

#
# Configure and build the ISL and CLooG libraries
#
%if %{with cloog}

%define isl_source %{builddir}/isl-%{isl_version}
%define isl_build %{builddir}/isl-build
%define isl_install %{builddir}/isl-install

mkdir %{isl_build} %{isl_install}
%ifarch s390 s390x
ISL_FLAG_PIC=-fPIC
%else
ISL_FLAG_PIC=-fpic
%endif
cd %{isl_build}
	%{isl_source}/configure \
		--disable-silent-rules \
		--disable-shared \
		CC="%{__cc}" \
		CXX="%{__cxx}" \
		CFLAGS="${CFLAGS:-%rpmcflags} $ISL_FLAG_PIC" \
		--prefix=%{isl_install}
	%{__make}
	%{__make} install
cd ..

%define cloog_source %{builddir}/cloog-%{cloog_version}
%define cloog_build %{builddir}/cloog-build
%define cloog_install %{builddir}/cloog-install

install -d %{cloog_build} %{builddir}/cloog-install
cd %{cloog_build}
cat >> %{cloog_source}/source/isl/constraints.c << \EOF
#include <isl/flow.h>
static void __attribute__((used)) *s1 = (void *) isl_union_map_compute_flow;
static void __attribute__((used)) *s2 = (void *) isl_map_dump;
EOF
sed -i 's|libcloog|libgcc49privatecloog|g' %{cloog_source}/{,test/}Makefile.{am,in}

%{cloog_source}/configure \
	--disable-silent-rules \
	--with-isl=system \
	--with-isl-prefix=%{isl_install} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="${CFLAGS:-%rpmcflags}" \
	CXXFLAGS="${CXXFLAGS:-%rpmcxxflags}" \
	--prefix=%{cloog_install}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make}
%{__make} install
cd %{cloog_install}/lib
rm libgcc49privatecloog-isl.so{,.4}
mv libgcc49privatecloog-isl.so.4.0.0 libcloog-isl.so.4
ln -sf libcloog-isl.so.4 libcloog-isl.so
ln -sf libcloog-isl.so.4 libcloog.so

%endif

#
# Configure the compiler
#
cd %{builddir}
config_target() {
	echo "=== CONFIGURING $1"

	arch=$1
	prefix=$arch-
	build_dir=$1

	case $arch in
	arm-*)		target=arm-linux-gnueabi;;
	aarch64-*)	target=aarch64-linux-gnu;;
	avr32-*)	target=avr-linux;;
	bfin-*)		target=bfin-uclinux;;
	c6x-*)		target=c6x-uclinux;;
	h8300-*)	target=h8300-elf;;
	mn10300-*)	target=am33_2.0-linux;;
	m68knommu-*)	target=m68k-linux;;
	openrisc-*)	target=or32-linux;;
	parisc-*)	target=hppa-linux;;
	score-*)	target=score-elf;;
	sh64-*)		target=sh64-linux;;
	tile-*)		target=tilegx-linux;;
	v850-*)		target=v850e-linux;;
	x86-*)		target=x86_64-linux;;
	*)		target=$arch;;
	esac

	echo $arch: target is $target
	#export CFLAGS="$RPM_OPT_FLAGS"

	CONFIG_FLAGS=
	case $arch in
	arm)
		CONFIG_FLAGS="--with-cpu=cortex-a8 --with-tune=cortex-a8 --with-arch=armv7-a --with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux"
		;;
	powerpc-*|powerpc64-*)
		CONFIG_FLAGS="--with-cpu-32=power4 --with-tune-32=power6 --with-cpu-64=power4 --with-tune-64=power6 --enable-secureplt"
		;;
	s390*-*)
		CONFIG_FLAGS="--with-arch=z9-109 --with-tune=z10 --enable-decimal-float"
		;;
	sh-*)
		CONFIG_FLAGS="--with-multilib-list=m1,m2,m2e,m4,m4-single,m4-single-only,m2a,m2a-single,!m2a,!m2a-single"
		;;
	sh64-*)
		CONFIG_FLAGS="--with-multilib-list=m5-32media,m5-32media-nofpu,m5-compact,m5-compact-nofpu,m5-64media,m5-64media-nofpu"
		;;
	sparc-*)
		CONFIG_FLAGS="--disable-linux-futex"
		;;
	tile-*)
		#CONFIG_FLAGS="--with-arch_32=tilepro"
		;;
	x86-*)
		CONFIG_FLAGS="--with-arch_32=i686"
		;;
	esac

	case $arch in
	alpha|powerpc*|s390*|sparc*)
		CONFIG_FLAGS="$CONFIG_FLAGS --with-long-double-128" ;;
	esac

	install -d $build_dir
	cd $build_dir

	# We could optimize the cross builds size by --enable-shared but the produced
	# binaries may be less convenient in the embedded environment.
	AR_FOR_TARGET=%{_bindir}/$arch-ar \
	AS_FOR_TARGET=%{_bindir}/$arch-as \
	DLLTOOL_FOR_TARGET=%{_bindir}/$arch-dlltool \
	LD_FOR_TARGET=%{_bindir}/$arch-ld \
	NM_FOR_TARGET=%{_bindir}/$arch-nm \
	OBJDUMP_FOR_TARGET=%{_bindir}/$arch-objdump \
	RANLIB_FOR_TARGET=%{_bindir}/$arch-ranlib \
	STRIP_FOR_TARGET=%{_bindir}/$arch-strip \
	WINDRES_FOR_TARGET=%{_bindir}/$arch-windres \
	WINDMC_FOR_TARGET=%{_bindir}/$arch-windmc \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="-Wl,-z,relro " \
	../%{srcdir}/configure \
	--bindir=%{_bindir} \
	--build=%{_target_platform} \
	--datadir=%{_datadir} \
	--disable-decimal-float \
	--disable-dependency-tracking \
	--disable-gold \
	--disable-libgomp \
	--disable-libmudflap \
	--disable-libquadmath \
	--disable-libssp \
	--disable-nls \
	--disable-plugin \
	--disable-shared \
	--disable-silent-rules \
	--disable-sjlj-exceptions \
	--disable-threads \
	--with-ld=/usr/bin/$arch-ld \
	--enable-checking=$checking \
	--enable-gnu-unique-object \
	--enable-initfini-array \
	--enable-languages=c,c++ \
	--enable-linker-build-id \
	--enable-nls \
	--enable-obsolete \
	--enable-targets=all \
	--exec-prefix=%{_exec_prefix} \
	--host=%{_target_platform} \
	--includedir=%{_includedir} \
	--infodir=%{_infodir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--program-prefix=$prefix \
	--sbindir=%{_sbindir} \
	--sharedstatedir=%{_sharedstatedir} \
	--sysconfdir=%{_sysconfdir} \
	--target=$target \
	--with-bugurl="http://bugs.pld-linux.org" \
	--with-linker-hash-style=gnu \
	--with-newlib \
	--with-sysroot=%{_prefix}/$arch/sys-root \
	--with-system-libunwind \
	--with-system-zlib \
	--without-headers \
%if %{with cloog}
	--with-isl=%{isl_install} --with-cloog=%{cloog_install} \
%else
	--without-isl --without-cloog \
%endif
	$CONFIG_FLAGS
%if 0
	--libdir=%{_libdir} # we want stuff in /usr/lib/gcc/ not /usr/lib64/gcc
%endif
	cd ..
}

for target in $(cat target.list); do
	config_target $target
done

build_target() {
	echo "=== BUILDING $1"

	arch=$1
	build_dir=$1

	AR_FOR_TARGET=%{_bindir}/$arch-ar \
	AS_FOR_TARGET=%{_bindir}/$arch-as \
	DLLTOOL_FOR_TARGET=%{_bindir}/$arch-dlltool \
	LD_FOR_TARGET=%{_bindir}/$arch-ld \
	NM_FOR_TARGET=%{_bindir}/$arch-nm \
	OBJDUMP_FOR_TARGET=%{_bindir}/$arch-objdump \
	RANLIB_FOR_TARGET=%{_bindir}/$arch-ranlib \
	STRIP_FOR_TARGET=%{_bindir}/$arch-strip \
	WINDRES_FOR_TARGET=%{_bindir}/$arch-windres \
	WINDMC_FOR_TARGET=%{_bindir}/$arch-windmc \
	%{__make} -C $build_dir tooldir=%{_prefix} all-gcc

	case $arch in
	%{no_libgcc_targets})
		;;
	*)
		%{__make} -C $build_dir tooldir=%{_prefix} all-target-libgcc
		;;
	esac
}

for target in $(cat target.list); do
	build_target $target
done

%install
rm -rf $RPM_BUILD_ROOT

install_bin() {
	echo "=== INSTALLING $1"

	arch=$1
	cpu=${1%%%%-*}

	case $arch in
	%{no_libgcc_targets})	with_libgcc="";;
	*)			with_libgcc="install-target-libgcc";;
	esac

	%{__make} -C $arch DESTDIR=$RPM_BUILD_ROOT install-gcc ${with_libgcc}

	# We want links for ppc and ppc64 also if we make powerpc or powerpc64
	case $cpu in
	powerpc*)
		cd $RPM_BUILD_ROOT%{_bindir}
			for i in $cpu-*; do
				ln -s $i ppc${i#powerpc}
			done
		cd -
		;;
	esac
}

for target in $(cat target.list); do
	install -d $RPM_BUILD_ROOT%{_prefix}/$target/sys-root
	install_bin $target
done

grep ^powerpc target.list | sed -e s/powerpc/ppc/ > symlink-target.list

# We have to copy cloog somewhere graphite can dlopen it from
%if %{with cloog}
for i in $RPM_BUILD_ROOT%{_prefix}/lib/gcc/*/%{version}; do
	cp -a %{cloog_install}/lib/libcloog-isl.so.4 $i
done
%endif

# For cross-gcc we drop the documentation.
rm -rf $RPM_BUILD_ROOT%{_infodir}

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
rm -f $RPM_BUILD_ROOT%{_libdir}/{libffi*,libiberty.a}
rm -f $RPM_BUILD_ROOT%{_libexecdir}/gcc/*/%{version}/install-tools/{mkheaders,fixincl}
rm -f $RPM_BUILD_ROOT%{_bindir}/*-gcc-%{version} || :
rm -f $RPM_BUILD_ROOT%{_bindir}/*-ar || :
rm -f $RPM_BUILD_ROOT%{_bindir}/*-nm || :
rm -f $RPM_BUILD_ROOT%{_bindir}/*-ranlib || :
rmdir  $RPM_BUILD_ROOT%{_includedir}

find $RPM_BUILD_ROOT%{_datadir} -name gcc.mo |
while read x; do
	y=$(dirname $x)
	mv $x $y/cross-gcc.mo
done

%find_lang cross-gcc

rm $RPM_BUILD_ROOT%{_mandir}/man7/*.7
rmdir $RPM_BUILD_ROOT%{_mandir}/man7

# All the installed manual pages and translation files for each program are the
# same, so symlink them to the common package
cd $RPM_BUILD_ROOT%{_mandir}/man1
	for i in cross-cpp.1 cross-gcc.1 cross-g++.1 cross-gcov.1; do
		j=${i#cross-}

		for k in *-$j; do
			if [ $k != $i -a ! -L $k ]; then
				mv $k $i
				ln -s $i $k
			fi
		done
	done

	# Add manpages the additional symlink-only targets
	%if %{with powerpc}%{with powerpc64}
	for i in powerpc*; do
		ln -s $i ppc${i#powerpc}
	done
	%endif
cd -

install_lang() {
	arch=$1
	cpu=${arch%%%%-*}

	case $cpu in
	avr32)		target_cpu=avr;;
	bfin)		target_cpu=bfin;;
	h8300)		target_cpu=h8300;;
	mn10300)	target_cpu=am33_2.0;;
	openrisc)	target_cpu=openrisc;;
	parisc)		target_cpu=hppa;;
	score)		target_cpu=score;;
	tile)		target_cpu=tilegx;;
	v850)		target_cpu=v850e;;
	x86)		target_cpu=x86_64;;
	*)		target_cpu=$cpu;;
	esac

	(
	echo "%%defattr(-,root,root,-)"
	echo "%{_bindir}/$arch*-cpp"
	echo "%{_bindir}/$arch*-gcc"
	echo "%{_bindir}/$arch*-gcov"
	echo "%{_mandir}/man1/$arch*-cpp*"
	echo "%{_mandir}/man1/$arch*-gcc*"
	echo "%{_mandir}/man1/$arch*-gcov*"
	case $cpu in
		ppc*|ppc64*)
		;;
		*)
		echo "/usr/lib/gcc/$target_cpu-*/"
		echo "%{_libexecdir}/gcc/$target_cpu*/*/cc1"
		echo "%{_libexecdir}/gcc/$target_cpu*/*/collect2"
		echo "%{_libexecdir}/gcc/$target_cpu*/*/[abd-z]*"
		echo "%{_prefix}/$arch/sys-root"
	esac

	) >files.$arch

	(
	echo "%%defattr(-,root,root,-)"
	echo "%{_bindir}/$arch*-c++"
	echo "%{_bindir}/$arch*-g++"
	echo "%{_mandir}/man1/$arch*-g++*"
	case $cpu in
		ppc*|ppc64*)
		;;
		*)
		echo "%{_libexecdir}/gcc/$target_cpu*/*/cc1plus"
	esac
	) > files-c++.$arch
}

for target in $(cat target.list symlink-target.list); do
	install_lang $target
done

%define __ar_no_strip $RPM_BUILD_DIR/%{name}-%{version}/ar-no-strip
cat >%{__ar_no_strip} <<'EOF'
#!/bin/sh
f=$2
if [ ${f##*/} = libgcc.a -o ${f##*/} = libgcov.a ]; then
	:
else
	%{__strip} $*
fi
EOF
chmod +x %{__ar_no_strip}
%undefine __strip
%define __strip %{__ar_no_strip}

%clean
rm -rf $RPM_BUILD_ROOT

%files common -f cross-gcc.lang
%doc %{srcdir}/COPYING*
%doc %{srcdir}/README
%{_mandir}/man1/cross-*

%define do_files() \
%files -n gcc-%1 -f files.%1 \
%files -n gcc-c++-%1 -f files-c++.%1 \

%{?with_alpha:%do_files alpha-linux-gnu}
%{?with_arm:%do_files arm-linux-gnu}
%{?with_aarch64:%do_files aarch64-linux-gnu}
%{?with_avr32:%do_files avr32-linux-gnu}
%{?with_blackfin:%do_files bfin-linux-gnu}
%{?with_c6x:%do_files c6x-linux-gnu}
%{?with_cris:%do_files cris-linux-gnu}
%{?with_frv:%do_files frv-linux-gnu}
%{?with_h8300:%do_files h8300-linux-gnu}
%{?with_hppa:%do_files hppa-linux-gnu}
%{?with_hppa64:%do_files hppa64-linux-gnu}
%{?with_i386:%do_files i386-linux-gnu}
%{?with_ia64:%do_files ia64-linux-gnu}
%{?with_m32r:%do_files m32r-linux-gnu}
%{?with_m68k:%do_files m68k-linux-gnu}
%{?with_metag:%do_files metag-linux-gnu}
%{?with_microblaze:%do_files microblaze-linux-gnu}
%{?with_mips:%do_files mips-linux-gnu}
%{?with_mips64:%do_files mips64-linux-gnu}
%{?with_mn10300:%do_files mn10300-linux-gnu}
%{?with_nios2:%do_files nios2-linux-gnu}
%{?with_openrisc:%do_files openrisc-linux-gnu}
%{?with_powerpc:%do_files powerpc-linux-gnu}
%{?with_powerpc64:%do_files powerpc64-linux-gnu}
%{?with_powerpc:%do_files ppc-linux-gnu}
%{?with_powerpc64:%do_files ppc64-linux-gnu}
%{?with_s390:%do_files s390-linux-gnu}
%{?with_s390x:%do_files s390x-linux-gnu}
%{?with_score:%do_files score-linux-gnu}
%{?with_sh:%do_files sh-linux-gnu}
%{?with_sh4:%do_files sh4-linux-gnu}
%{?with_sh64:%do_files sh64-linux-gnu}
%{?with_sparc:%do_files sparc-linux-gnu}
%{?with_sparc64:%do_files sparc64-linux-gnu}
%{?with_tile:%do_files tile-linux-gnu}
%{?with_unicore32:%do_files unicore32-linux-gnu}
%{?with_x86_64:%do_files x86_64-linux-gnu}
%{?with_xtensa:%do_files xtensa-linux-gnu}
