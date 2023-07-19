
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="fastplot",
    description="Are you bored of re-writing code for each plot? Create publication-quality plots with a simple interface over matplotlib.",
    license="GNU GENERAL PUBLIC LICENSE v3",
    version="1.3.0",
    author="Martino Trevisan",
    author_email="martino.trevisan@polito.it",
    maintainer="Martino Trevisan",
    maintainer_email="martino.trevisan@polito.it",
    url="https://github.com/marty90/fastplot",
    download_url = 'https://github.com/marty90/fastplot/tarball/1.3.0',
    packages=['fastplot'],
    install_requires=['matplotlib', 'numpy', 'pandas', 'statsmodels', 'scipy', 'seaborn']
)

# Upload on pip with:
# Create new version
# python setup.py sdist
# twine upload dist/*

# Test it locally removing the pip installed one
