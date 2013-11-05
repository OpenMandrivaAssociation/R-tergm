%global packname  tergm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.1.0
Release:          1
Summary:          Fit, Simulate and Diagnose Models for Network Evoluation
Group:            Sciences/Mathematics
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.1-0.tar.gz

Requires:         R-statnet.common R-ergm R-robustbase R-nlme R-network R-networkDynamic R-coda 

Requires:         R-lattice R-snow 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-statnet.common R-ergm R-robustbase R-nlme R-network R-networkDynamic R-coda

BuildRequires:   R-lattice R-snow 
%description
An integrated set of extensions to the `ergm` package to analyze and
simulate network evolution based on exponential-family random graph models
(ERGM). "tergm" is a part of the "statnet" suite of packages for network

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS*
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
