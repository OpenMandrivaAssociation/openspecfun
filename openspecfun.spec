%define debug_package %{nil}

%define libname %mklibname openspecfun 1 
%define devname %mklibname -d openspecfun

Summary:        Library providing a collection of special mathematical functions
Name:           openspecfun
Version:        0.5.3
Release:        2
License:        MIT and Public Domain
Group:          System/Libraries
Source0:        https://github.com/JuliaLang/openspecfun/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:            https://github.com/JuliaLang/openspecfun
BuildRequires:  gcc-gfortran

%description
Currently provides AMOS and Faddeeva. AMOS (from Netlib) is a
portable package for Bessel Functions of a Complex Argument and
Nonnegative Order; it contains subroutines for computing Bessel
functions and Airy functions. Faddeeva allows computing the
various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled
complementary error function, imaginary error function, and Dawson function);
given these, one can also easily compute Voigt functions, Fresnel integrals,
and similar related functions as well.

%package -n %libname

%package -n %devname
Summary:    Library providing a collection of special mathematical functions
Group:      Development/C
Requires:   %{libname} = %{version}-%{release}
Provides:   %{name}-devel

%description -n %devname
Contains header files for developing applications that use the %{name}
library.

%prep
%setup -q %{name}-%{version}

%build
make %{?_smp_mflags} \
      FFLAGS="%{optflags}" \
      CFLAGS="%{optflags}" \
      USE_OPENLIBM=0 \
      includedir=%{_includedir}

%install
make install prefix=%{_prefix} \
             libdir=%{_libdir} \
             includedir=%{_includedir} \
             DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.a

%files -n %libname
%doc LICENSE.md README.md
%{_libdir}/libopenspecfun.so.1*

%files -n %devname
%{_libdir}/libopenspecfun.so
%{_includedir}/Faddeeva.h

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.3-2
- Rebuild for gfortran 7.

* Wed Jul 27 2016 Milan Bouchet-Valat <nalimilan@club.fr> - 0.5.3-1
- New upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 27 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.4-1
- New upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 1 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.3-1
- New upstream release.
- Use Group System Environment/Libraries for base package.

* Fri Feb 14 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.2-2
- Don't build static libraries package by default.

* Sat Feb 8 2014 Milan Bouchet-Valat <nalimilan@club.fr> - 0.2-1
- Initial version.
