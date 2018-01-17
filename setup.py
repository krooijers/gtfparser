from setuptools import setup
from Cython.Build import cythonize

setup(
    name='gtfparser',

    version='0.1.0',

    description='python3 GTF (GFF2) parser that aims to be fast',

    author='K. Rooijers',
    author_email='k.rooijers@hubrecht.eu',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='bioinformatics',

    py_modules=["gtfparser"],
    ext_modules=cythonize(["attrsplitter.pyx"]),

    install_requires=["cython"],
)
