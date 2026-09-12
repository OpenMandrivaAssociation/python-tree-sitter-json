Name:		python-tree-sitter-json
Version:	0.24.8
Release:	1
Summary:	Tree-sitter json grammar (Python bindings)
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/tree-sitter-json
Source0:	https://files.pythonhosted.org/packages/d7/29/e92df6dca3a6b2ab1c179978be398059817e1173fbacd47e832aaff3446b/tree_sitter_json-0.24.8.tar.gz
# PyPI sdist omits src/tree_sitter/*.h
Source1:	tree-sitter-c-headers.tar.xz
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	clang
Requires:	python%{pyver}dist(tree-sitter)

%description
Tree-sitter grammar for json, compiled from source. Used by
Aider's grep-ast repo-map.

%prep
%autosetup -n tree_sitter_json-0.24.8
tar -C src -xf %{SOURCE1}

%build

%install
export CC=clang
python -m pip install \
	--no-deps --no-build-isolation --no-compile \
	--root %{buildroot} --prefix %{_prefix} \
	.

%files
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter_json*
