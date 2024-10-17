Name:		texlive-latexcheat-ptbr
Version:	15878
Release:	2
Summary:	A LaTeX cheat sheet, in Brazilian Portuguese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latexcheat/latexcheat-ptbr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
