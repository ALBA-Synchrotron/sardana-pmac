from setuptools import setup, find_packages


setup(
    name="sardana-pmac",
    version="0.2.1",
    description="Pmac Sardana plugins (controllers, macros, tools)",
    author="ALBA controls team",
    author_email="controls@cells.es",
    license="GPLv3",
    url="http://github.com/ALBA-Synchrotron/sardana-pmac",
    packages=find_packages(),
    install_requires=["sardana", ],
    python_requires=">=3.5",
)
