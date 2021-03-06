from setuptools import find_packages, setup

setup(
    name="my_gym",
    packages=[package for package in find_packages() if package.startswith("my_gym")],
    url="https://github.com/osigaud/my_gym",
    version="0.0.1",
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
    author="Olivier Sigaud",
    author_email="Olivier.Sigaud@isir.upmc.fr",
    license="MIT",
    description="A set of additional gym environments",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt", "r").read().splitlines(),
)
