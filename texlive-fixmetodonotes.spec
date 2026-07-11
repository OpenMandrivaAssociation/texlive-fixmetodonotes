%global tl_name fixmetodonotes
%global tl_revision 30168

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.2
Release:	%{tl_revision}.1
Summary:	Add notes on document development
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixmetodonotes
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixmetodonotes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools to highlight FIXME and TODO annotations. The
command \listofnotes prints a list of outstanding notes, with links to
the pages on which they appear.

