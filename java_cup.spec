
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
Release:	15.1
License:	GPLv3+
Source0:	java_cup-0.11a-15.1-omv2014.1.noarch.rpm
Source1:	java_cup-javadoc-0.11a-15.1-omv2014.1.noarch.rpm
Source2:	java_cup-manual-0.11a-15.1-omv2014.1.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/java_cup
BuildArch:	noarch
Summary:	java_cup bootstrap version
#Requires:	javapackages-bootstrap
Requires:	java
Requires:	jpackage-utils
Provides:	java_cup = 1:0.11a-15.1:2014.1
Provides:	mvn(java_cup:java_cup) = 0.11a
Provides:	osgi(java_cup) = 0.11.0
Provides:	osgi(java_cup.runtime) = 0.11.0

%description
java_cup bootstrap version.

%files
/usr/share/doc/java_cup
/usr/share/doc/java_cup/LICENSE.txt
/usr/share/doc/java_cup/changelog.txt
/usr/share/java/java_cup-runtime.jar
/usr/share/java/java_cup.jar
/usr/share/maven-fragments/java_cup
/usr/share/maven-poms/JPP-java_cup.pom

#------------------------------------------------------------------------
%package	-n java_cup-javadoc
Epoch:		1
Version:	0.11a
Release:	15.1
Summary:	java_cup-javadoc bootstrap version
#Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	java_cup-javadoc = 1:0.11a-15.1:2014.1

%description	-n java_cup-javadoc
java_cup-javadoc bootstrap version.

%files		-n java_cup-javadoc
/usr/share/doc/java_cup-javadoc
/usr/share/doc/java_cup-javadoc/LICENSE.txt
/usr/share/javadoc/java_cup
/usr/share/javadoc/java_cup/allclasses-frame.html
/usr/share/javadoc/java_cup/allclasses-noframe.html
/usr/share/javadoc/java_cup/constant-values.html
/usr/share/javadoc/java_cup/deprecated-list.html
/usr/share/javadoc/java_cup/help-doc.html
/usr/share/javadoc/java_cup/index-all.html
/usr/share/javadoc/java_cup/index.html
/usr/share/javadoc/java_cup/java_cup
/usr/share/javadoc/java_cup/java_cup/ErrorManager.html
/usr/share/javadoc/java_cup/java_cup/Main.html
/usr/share/javadoc/java_cup/java_cup/action_part.html
/usr/share/javadoc/java_cup/java_cup/action_production.html
/usr/share/javadoc/java_cup/java_cup/anttask
/usr/share/javadoc/java_cup/java_cup/anttask/CUPTask.html
/usr/share/javadoc/java_cup/java_cup/anttask/class-use
/usr/share/javadoc/java_cup/java_cup/anttask/class-use/CUPTask.html
/usr/share/javadoc/java_cup/java_cup/anttask/package-frame.html
/usr/share/javadoc/java_cup/java_cup/anttask/package-summary.html
/usr/share/javadoc/java_cup/java_cup/anttask/package-tree.html
/usr/share/javadoc/java_cup/java_cup/anttask/package-use.html
/usr/share/javadoc/java_cup/java_cup/assoc.html
/usr/share/javadoc/java_cup/java_cup/class-use
/usr/share/javadoc/java_cup/java_cup/class-use/ErrorManager.html
/usr/share/javadoc/java_cup/java_cup/class-use/Main.html
/usr/share/javadoc/java_cup/java_cup/class-use/action_part.html
/usr/share/javadoc/java_cup/java_cup/class-use/action_production.html
/usr/share/javadoc/java_cup/java_cup/class-use/assoc.html
/usr/share/javadoc/java_cup/java_cup/class-use/emit.html
/usr/share/javadoc/java_cup/java_cup/class-use/internal_error.html
/usr/share/javadoc/java_cup/java_cup/class-use/lalr_item.html
/usr/share/javadoc/java_cup/java_cup/class-use/lalr_item_set.html
/usr/share/javadoc/java_cup/java_cup/class-use/lalr_state.html
/usr/share/javadoc/java_cup/java_cup/class-use/lalr_transition.html
/usr/share/javadoc/java_cup/java_cup/class-use/lr_item_core.html
/usr/share/javadoc/java_cup/java_cup/class-use/non_terminal.html
/usr/share/javadoc/java_cup/java_cup/class-use/nonassoc_action.html
/usr/share/javadoc/java_cup/java_cup/class-use/parse_action.html
/usr/share/javadoc/java_cup/java_cup/class-use/parse_action_row.html
/usr/share/javadoc/java_cup/java_cup/class-use/parse_action_table.html
/usr/share/javadoc/java_cup/java_cup/class-use/parse_reduce_row.html
/usr/share/javadoc/java_cup/java_cup/class-use/parse_reduce_table.html
/usr/share/javadoc/java_cup/java_cup/class-use/production.html
/usr/share/javadoc/java_cup/java_cup/class-use/production_part.html
/usr/share/javadoc/java_cup/java_cup/class-use/reduce_action.html
/usr/share/javadoc/java_cup/java_cup/class-use/shift_action.html
/usr/share/javadoc/java_cup/java_cup/class-use/symbol.html
/usr/share/javadoc/java_cup/java_cup/class-use/symbol_part.html
/usr/share/javadoc/java_cup/java_cup/class-use/symbol_set.html
/usr/share/javadoc/java_cup/java_cup/class-use/terminal.html
/usr/share/javadoc/java_cup/java_cup/class-use/terminal_set.html
/usr/share/javadoc/java_cup/java_cup/class-use/version.html
/usr/share/javadoc/java_cup/java_cup/emit.html
/usr/share/javadoc/java_cup/java_cup/internal_error.html
/usr/share/javadoc/java_cup/java_cup/lalr_item.html
/usr/share/javadoc/java_cup/java_cup/lalr_item_set.html
/usr/share/javadoc/java_cup/java_cup/lalr_state.html
/usr/share/javadoc/java_cup/java_cup/lalr_transition.html
/usr/share/javadoc/java_cup/java_cup/lr_item_core.html
/usr/share/javadoc/java_cup/java_cup/non_terminal.html
/usr/share/javadoc/java_cup/java_cup/nonassoc_action.html
/usr/share/javadoc/java_cup/java_cup/package-frame.html
/usr/share/javadoc/java_cup/java_cup/package-summary.html
/usr/share/javadoc/java_cup/java_cup/package-tree.html
/usr/share/javadoc/java_cup/java_cup/package-use.html
/usr/share/javadoc/java_cup/java_cup/parse_action.html
/usr/share/javadoc/java_cup/java_cup/parse_action_row.html
/usr/share/javadoc/java_cup/java_cup/parse_action_table.html
/usr/share/javadoc/java_cup/java_cup/parse_reduce_row.html
/usr/share/javadoc/java_cup/java_cup/parse_reduce_table.html
/usr/share/javadoc/java_cup/java_cup/production.html
/usr/share/javadoc/java_cup/java_cup/production_part.html
/usr/share/javadoc/java_cup/java_cup/reduce_action.html
/usr/share/javadoc/java_cup/java_cup/runtime
/usr/share/javadoc/java_cup/java_cup/runtime/ComplexSymbolFactory.ComplexSymbol.html
/usr/share/javadoc/java_cup/java_cup/runtime/ComplexSymbolFactory.Location.html
/usr/share/javadoc/java_cup/java_cup/runtime/ComplexSymbolFactory.html
/usr/share/javadoc/java_cup/java_cup/runtime/DefaultSymbolFactory.html
/usr/share/javadoc/java_cup/java_cup/runtime/Scanner.html
/usr/share/javadoc/java_cup/java_cup/runtime/Symbol.html
/usr/share/javadoc/java_cup/java_cup/runtime/SymbolFactory.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/ComplexSymbolFactory.ComplexSymbol.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/ComplexSymbolFactory.Location.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/ComplexSymbolFactory.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/DefaultSymbolFactory.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/Scanner.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/Symbol.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/SymbolFactory.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/lr_parser.html
/usr/share/javadoc/java_cup/java_cup/runtime/class-use/virtual_parse_stack.html
/usr/share/javadoc/java_cup/java_cup/runtime/lr_parser.html
/usr/share/javadoc/java_cup/java_cup/runtime/package-frame.html
/usr/share/javadoc/java_cup/java_cup/runtime/package-summary.html
/usr/share/javadoc/java_cup/java_cup/runtime/package-tree.html
/usr/share/javadoc/java_cup/java_cup/runtime/package-use.html
/usr/share/javadoc/java_cup/java_cup/runtime/virtual_parse_stack.html
/usr/share/javadoc/java_cup/java_cup/shift_action.html
/usr/share/javadoc/java_cup/java_cup/symbol.html
/usr/share/javadoc/java_cup/java_cup/symbol_part.html
/usr/share/javadoc/java_cup/java_cup/symbol_set.html
/usr/share/javadoc/java_cup/java_cup/terminal.html
/usr/share/javadoc/java_cup/java_cup/terminal_set.html
/usr/share/javadoc/java_cup/java_cup/version.html
/usr/share/javadoc/java_cup/overview-frame.html
/usr/share/javadoc/java_cup/overview-summary.html
/usr/share/javadoc/java_cup/overview-tree.html
/usr/share/javadoc/java_cup/package-list
/usr/share/javadoc/java_cup/resources
/usr/share/javadoc/java_cup/resources/background.gif
/usr/share/javadoc/java_cup/resources/tab.gif
/usr/share/javadoc/java_cup/resources/titlebar.gif
/usr/share/javadoc/java_cup/resources/titlebar_end.gif
/usr/share/javadoc/java_cup/serialized-form.html
/usr/share/javadoc/java_cup/stylesheet.css

#------------------------------------------------------------------------
%package	-n java_cup-manual
Epoch:		1
Version:	0.11a
Release:	15.1
Summary:	java_cup-manual bootstrap version
#Requires:	javapackages-bootstrap
Provides:	java_cup-manual = 1:0.11a-15.1:2014.1

%description	-n java_cup-manual
java_cup-manual bootstrap version.

%files		-n java_cup-manual
/usr/share/doc/java_cup-manual
/usr/share/doc/java_cup-manual/LICENSE.txt
/usr/share/doc/java_cup-manual/manual.html

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
