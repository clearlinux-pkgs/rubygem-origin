#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-origin
Version  : 2.1.1
Release  : 2
URL      : https://rubygems.org/downloads/origin-2.1.1.gem
Source0  : https://rubygems.org/downloads/origin-2.1.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
Origin [![Build Status](https://secure.travis-ci.org/mongoid/origin.png?branch=master&.png)](http://travis-ci.org/mongoid/origin) [![Code Climate](https://codeclimate.com/github/mongoid/origin.png)](https://codeclimate.com/github/mongoid/origin) [![Coverage Status](https://coveralls.io/repos/mongoid/origin/badge.png?branch=master)](https://coveralls.io/r/mongoid/origin?branch=master)
========

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n origin-2.1.1
gem spec %{SOURCE0} -l --ruby > rubygem-origin.gemspec

%build
gem build rubygem-origin.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
origin-2.1.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/origin-2.1.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/ActiveSupport/cdesc-ActiveSupport.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Boolean/cdesc-Boolean.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/aggregating%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/aggregating-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/aggregation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/cdesc-Aggregable.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/pipeline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/project-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Aggregable/unwind-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__add__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__array__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__deep_copy__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__evolve_date__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__expand_complex__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__intersect__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__sort_option__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/__sort_pair__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/cdesc-Array.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/multi-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Array/update_values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/BigDecimal/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/BigDecimal/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/BigDecimal/cdesc-BigDecimal.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Boolean/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Boolean/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Boolean/cdesc-Boolean.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Date/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Date/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Date/__evolve_date__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Date/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Date/cdesc-Date.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/DateTime/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/DateTime/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/DateTime/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/DateTime/cdesc-DateTime.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__add__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__add_from_array__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__deep_copy__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__expand_complex__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__intersect__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__intersect_from_array__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__intersect_from_object__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__sort_option__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__union__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/__union_from_object__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/apply_strategy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/cdesc-Hash.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Hash/update_values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/__add__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/__evolve_date__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/__expanded__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/__intersect__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/__override__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/__union__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/NilClass/cdesc-NilClass.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Numeric/ClassMethods/__numeric__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Numeric/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Numeric/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Numeric/__evolve_date__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Numeric/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Numeric/cdesc-Numeric.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Numeric/to_direction-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/ClassMethods/__evolve__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__add__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__add_from_array__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__array__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__deep_copy__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__expand_complex__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__intersect__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__intersect_from_array__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__intersect_from_object__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__union__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/__union_from_object__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Object/regexp%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Range/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Range/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Range/__array__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Range/__evolve_date__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Range/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Range/cdesc-Range.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Regexp/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Regexp/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Regexp/cdesc-Regexp.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Regexp/regexp%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Set/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Set/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Set/cdesc-Set.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/ClassMethods/__expr_part__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/__evolve_date__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/__expr_part__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/__mongo_expression__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/__sort_option__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/String/to_direction-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Symbol/ClassMethods/add_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Symbol/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Symbol/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Symbol/__expr_part__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Symbol/cdesc-Symbol.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Symbol/to_direction-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Time/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Time/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Time/__evolve_date__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Time/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/Time/cdesc-Time.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/TimeWithZone/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/TimeWithZone/ClassMethods/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/TimeWithZone/__evolve_time__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/TimeWithZone/cdesc-TimeWithZone.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Extensions/cdesc-Extensions.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Forwardable/__forward__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Forwardable/cdesc-Forwardable.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Forwardable/select_with-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/__expr_part__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/__sort_option__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/__sort_pair__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/block-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/cdesc-Key.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/eql%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/expanded-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/operator-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/strategy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Key/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Macroable/cdesc-Macroable.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Macroable/key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/__add__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/__expanded__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/__intersect__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/__merge__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/__multi__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/__override__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/__union__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/cdesc-Mergeable.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/intersect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/override-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/prepare-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/reset_strategies%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/strategy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/union-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/use-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Mergeable/with_strategy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/add_sort_option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/asc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/ascending-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/batch_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/cdesc-Optional.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/desc-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/descending-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/forwardables-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/hint-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/limit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/max_scan-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/no_timeout-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/offset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/only-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/option-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/order-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/order_by-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/reorder-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/slice-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/snapshot-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/sort_with_list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Optional/without-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/cdesc-Options.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/evolve_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/fields-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/limit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/skip-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/sort-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/store-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Options/to_pipeline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/__deep_copy__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/aliases-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/cdesc-Pipeline.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/group-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/project-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Pipeline/unwind-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Queryable/%3d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Queryable/aliases-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Queryable/cdesc-Queryable.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Queryable/driver-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Queryable/initialize_copy-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Queryable/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Queryable/serializers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/all_in-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/all_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/and-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/any_in-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/any_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/between-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/cdesc-Selectable.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/elem_match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/excludes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/exists-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/expr_query-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/forwardables-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/geo_spacial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/gt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/gte-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/in-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/js_query-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/lt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/lte-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/max_distance-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/mod-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/ne-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/near-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/near_sphere-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/negating%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/negating-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/nin-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/nor-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/not-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/not_in-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/or-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/selection-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/selector-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/typed_override-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/where-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/with_array_values-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/with_size-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selectable/with_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/cdesc-Selector.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/evolve-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/evolve_array-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/evolve_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/evolve_multi-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/merge%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/multi_selection%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/store-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Selector/to_pipeline-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/__deep_copy__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/aliases-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/cdesc-Smash.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/normalized_key-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/serializers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/Smash/storage_pair-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/Origin/cdesc-Origin.ri
/usr/lib64/ruby/gems/2.2.0/doc/origin-2.1.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/aggregable.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/array.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/big_decimal.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/boolean.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/date.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/date_time.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/hash.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/nil_class.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/numeric.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/object.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/range.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/regexp.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/set.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/string.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/symbol.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/time.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/extensions/time_with_zone.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/forwardable.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/key.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/macroable.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/mergeable.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/optional.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/options.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/pipeline.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/queryable.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/selectable.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/selector.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/smash.rb
/usr/lib64/ruby/gems/2.2.0/gems/origin-2.1.1/lib/origin/version.rb
/usr/lib64/ruby/gems/2.2.0/specifications/origin-2.1.1.gemspec
