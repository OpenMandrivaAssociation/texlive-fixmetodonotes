Name:		texlive-fixmetodonotes
Version:	30168
Release:	2
Summary:	Add notes on document development
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixmetodonotes
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools to highlight FIXME and TODO
annotations. The command \listofnotes prints a list of
outstanding notes, with links to the pages on which they
appear.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fixmetodonotes/fixmetodonotes.sty
%doc %{_texmfdistdir}/doc/latex/fixmetodonotes/LICENSE
%doc %{_texmfdistdir}/doc/latex/fixmetodonotes/README
#- source
%doc %{_texmfdistdir}/source/latex/fixmetodonotes/fixmetodonotes.dtx
%doc %{_texmfdistdir}/source/latex/fixmetodonotes/fixmetodonotes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
