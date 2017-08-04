# Generated from backports-3.6.8.gem by gem2rpm -*- rpm-spec -*-
%global gem_name backports

Name: rubygem-%{gem_name}
Version: 3.6.8
Release: 2%{?dist}
Summary: Backports of Ruby features for older Ruby
Group: Development/Languages
License: MIT
URL: http://github.com/marcandre/backports
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# the following BuildRequires are development dependencies
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Essential backports that enable many of the nice features of Ruby 1.8.7 up to
2.1.0 for earlier versions.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.gitmodules
%exclude %{gem_instdir}/.irbrc
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/default.mspec
%{gem_libdir}
%{gem_instdir}/set_version
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/backports.gemspec
%{gem_instdir}/spec
%{gem_instdir}/test

%changelog
* Fri Sep 23 2016 Rich Megginson <rmeggins@redhat.com> - 3.6.8-2
- bump rel to rebuild for rhlog-buildrequires

* Thu Sep 22 2016 Rich Megginson <rmeggins@redhat.com> - 3.6.8-1
- Initial package
