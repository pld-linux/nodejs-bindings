%define		pkg	bindings
Summary:	Helper module for loading your native module's .node file
Name:		nodejs-%{pkg}
Version:	1.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/bindings/-/%{pkg}-%{version}.tgz
# Source0-md5:	52921674f0d3a9f69f058f99fa12847d
Patch0:		load-path.patch
URL:		https://github.com/TooTallNate/node-bindings
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a helper module for authors of Node.js native addon modules.
It is basically the "swiss army knife" of `require()`ing your native
module's `.node` file.

Throughout the course of Node's native addon history, addons have
ended up being compiled in a variety of different places, depending on
which build tool and which version of node was used. To make matters
worse, now the _gyp_ build tool can produce either a _Release_ or
_Debug_ build, each being built into different locations.

This module checks _all_ the possible locations that a native addon
would be built at, and returns the first one that loads successfully.

%prep
%setup -qc
mv package/* .
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p bindings.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
