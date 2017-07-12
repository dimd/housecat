from setuptools import setup, find_packages

setup(
    name='s2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-pymongo'
    ],
    tests_requires=[
        'pytest',
    ],
)
