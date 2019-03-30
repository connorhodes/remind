from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name = 'alarm',
    version = '0.0.0',
    description = 'reminder program',
    long_description = readme,
    author = "Ken Kundert",
    author_email = 'alarm@nurdletech.com',
    download_url = 'https://github.com/kenkundert/alarm/tarball/master',
    license = 'GPLv3+',
    zip_safe = True,
    py_modules = 'quantiphy'.split(),
    install_requires = 'docopt inform quantiphy arrow'.split(),
    python_requires = '>=3.6',
)
