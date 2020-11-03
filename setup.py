from cmaketools import setup

setup(
    name="TFC",
    version="0.0.1",
    author="Carl Leake and Hunter Johnston",
    author_email="leakec57@gmail.com",
    description="Theory of Functional Connections (TFC): A functional interpolation framework with applications in differential equations.",
    url="https://github.com/leakec/tfc.git",
    license="MIT",
    classifiers = ["Development Status :: 4 - Beta",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Programming Language :: C++",
                   "Programming Language :: Python :: 3 :: Only",
                   "Topic :: Scientific/Engineering",
                   "Topic :: Education"],
    src_dir="src",
    test_dir="tests",
    ext_module_dirs=["cxx","swig","python"],
    has_package_data=False,
    install_requires=["cmaketools>=0.1.6",
                      "setuptools>=50.3.2",
                      "numpy",
                      "jax",
                      "jaxlib",
                      "matplotlib",
                      "colorama",
                      "graphviz",
                      "yattag"],
)
