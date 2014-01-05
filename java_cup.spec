
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		java_cup
Epoch:		1
Version:	0.11a
Release:	15.0
Summary:	javapackages-bootstrap packages
License:	GPLv3+
Source0:	java_cup-0.11a-15.0-omv2014.0.noarch.rpm
URL:		https://abf.rosalinux.ru/openmandriva/java_cup
Summary:	java_cup bootstrap version
Requires:	javapackages-bootstrap
Requires:	java
Requires:	jpackage-utils
Provides:	java_cup = 1:0.11a-15.0:2014.0
Provides:	mvn(java_cup:java_cup) = 0.11a
Provides:	osgi(java_cup) = 0.11.0
Provides:	osgi(java_cup.runtime) = 0.11.0

%description
java_cup bootstrap version.

%files		-n java_cup
/usr/share/doc/java_cup
/usr/share/doc/java_cup/LICENSE.txt
/usr/share/doc/java_cup/changelog.txt
/usr/share/java/java_cup-runtime.jar
/usr/share/java/java_cup.jar
/usr/share/maven-fragments/java_cup
/usr/share/maven-poms/JPP-java_cup.pom

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
