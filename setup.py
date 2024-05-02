from setuptools import setup, find_packages

VERSION = "1.0"
DESCRIPTION = "Teste de pacote"


setup(
    name="Sorting-algorithms-from-aed",
    version=VERSION,
    description=DESCRIPTION,
    long_description= DESCRIPTION,
    author="arthur suzuki",
    author_email="ajls@cesar.school",
    packages=find_packages(),
    keywords=["Sorting Algorithms", "AED"]
)

# python setup.py sdist bdist_wheel

