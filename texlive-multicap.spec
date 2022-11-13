Name:		texlive-multicap
Version:	15878
Release:	1
Summary:	Format captions inside multicols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multicap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicap.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a package for formatting captions of column figures and
column tabular material, which cannot be standard floats in a
multicols environment. The package also provides a convenient
way to customise your captions, whether they be in multicols or
not.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multicap/multicap.sty
%doc %{_texmfdistdir}/doc/latex/multicap/multicap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/multicap/multicap.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
