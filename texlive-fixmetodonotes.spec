# revision 27053
# category Package
# catalog-ctan /macros/latex/contrib/fixmetodonotes
# catalog-date 2012-07-03 11:28:15 +0200
# catalog-license pd
# catalog-version 0.1
Name:		texlive-fixmetodonotes
Version:	0.1
Release:	1
Summary:	Add notes on document development
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fixmetodonotes
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
