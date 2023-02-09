from setuptools import setup, find_packages
import os

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


def get_version():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "VERSION"
    )
    g = {}
    with open(path) as fp:
        exec(fp.read(), g)
    return g["__version__"]


setup(
    name="edtf",
    version="0.0.2",
    description="Python package wrapping the `sfomuseum/go-edtf` WASM (WASI) binary for parsing Library of Congress Extended DateTime (EDTF) strings.",
    author="SFO Museum",
    license="Apache License, Version 2.0",
    url="https://github.com/sfomuseum/py-edtf",
    project_urls={
        "Source code": "https://github.com/sfomuseum/py-edtf",
        "Issues": "https://github.com/sfomuseum/py-edtf/issues",
    },
    packages=['edtf'],
    package_dir={'edtf': 'src/edtf'},
    package_data={'edtf': ['wasi/*.wasm']},
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "wasmer",
        "importlib_resources",
    ]
)
