from setuptools import setup, find_packages

setup(
    name='geoservice',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires='requirements.txt'
)
