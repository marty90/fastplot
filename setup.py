
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="fastplot",
    description="Are you bored of re-writing code for each plot? Create publication-quality plots with a simple interface over matplotlib.",
    license="GNU GENERAL PUBLIC LICENSE v3",
    version="1.0.5",
    author="Martino Trevisan",
    author_email="martino.trevisan@polito.it",
    maintainer="Martino Trevisan",
    maintainer_email="martino.trevisan@polito.it",
    url="https://github.com/marty90/fastplot",
    download_url = 'https://github.com/marty90/fastplot/tarball/1.0.5',
    packages=['fastplot'],
    install_requires=['matplotlib', 'numpy', 'pandas', 'statsmodels', 'scipy']
)

# Upload on pip with:
# python setup.py sdist
# twine upload dist/*

# Install locally with:
# sudo python3 setup.py install
