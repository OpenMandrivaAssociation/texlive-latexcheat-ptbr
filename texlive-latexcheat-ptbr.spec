%global tl_name latexcheat-ptbr
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.13
Release:	%{tl_revision}.1
Summary:	A LaTeX cheat sheet, in Brazilian Portuguese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latexcheat/latexcheat-ptbr
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcheat-ptbr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a translation to Brazilian Portuguese of Winston Chang's LaTeX
cheat sheet

