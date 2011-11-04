# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/multicap
# catalog-date 2006-12-15 15:26:27 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-multicap
Version:	20061215
Release:	1
Summary:	Format captions inside multicols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multicap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multicap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This is a package for formatting captions of column figures and
column tabular material, which cannot be standard floats in a
multicols environment. The package also provides a convenient
way to customise your captions, whether they be in multicols or
not.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multicap/multicap.sty
%doc %{_texmfdistdir}/doc/latex/multicap/multicap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/multicap/multicap.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
