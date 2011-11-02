Name:		texlive-latexcheat-ptbr
Version:	1.13
Release:	1
Summary:	A LaTeX cheat sheet, in Brazilian Portuguese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latexcheat/latexcheat-ptbr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
