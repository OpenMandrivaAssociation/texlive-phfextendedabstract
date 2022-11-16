Name:		texlive-phfextendedabstract
Version:	60732
Release:	1
Summary:	Typeset extended abstracts for conferences, such as often encountered in quantum information theory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfextendedabstract
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfextendedabstract.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfextendedabstract.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfextendedabstract.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Several conferences in various fields (such as quantum
information theory) require the submission of extended
abstracts. An extended abstract is a summary of a scientific
result, presented at a high level, and consisting of at most a
small handful of pages. The phfextendedabstract LaTeX class
provides a simple style for such abstracts. There are only two
sectioning levels, sections and paragraphs, and the style is
optimized to save space as well as to guide the reader's eye
through the overall structure of the document. An option will
try to compress all vertical space to save some space, in case
you need to satisfy page constraints. The style builds upon the
powerful RevTeX class, so you can use all of RevTeX's features
such as author affiliations, etc.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfextendedabstract
%{_texmfdistdir}/tex/latex/phfextendedabstract
%doc %{_texmfdistdir}/doc/latex/phfextendedabstract

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
