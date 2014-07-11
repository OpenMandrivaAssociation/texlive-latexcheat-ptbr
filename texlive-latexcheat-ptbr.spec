# revision 15878
# category Package
# catalog-ctan /info/latexcheat/latexcheat-ptbr
# catalog-date 2009-04-10 11:30:41 +0200
# catalog-license lppl
# catalog-version 1.13
Name:		texlive-latexcheat-ptbr
Version:	1.13
Release:	8
Summary:	A LaTeX cheat sheet, in Brazilian Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexcheat/latexcheat-ptbr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a translation to Brazilian Portuguese of Winston
Chang's LaTeX cheat sheet.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latexcheat-ptbr/README-ptbr
%doc %{_texmfdistdir}/doc/latex/latexcheat-ptbr/latexsheet-ptbr.pdf
%doc %{_texmfdistdir}/doc/latex/latexcheat-ptbr/latexsheet-ptbr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.13-2
+ Revision: 753139
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.13-1
+ Revision: 718816
- texlive-latexcheat-ptbr
- texlive-latexcheat-ptbr
- texlive-latexcheat-ptbr
- texlive-latexcheat-ptbr

