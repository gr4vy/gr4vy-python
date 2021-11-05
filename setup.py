import setuptools
from setuptools import setup,find_packages

setup(
    name="gr4vy_python",
    version="0.0.1",
    packages=find_packages(),
    author="gr4vy",
    author_email="phillip@gr4vy.com",
    description="Gr4vy Python",
    url="https://github.com/gr4vy/gr4vy-python",
    project_urls={
        "Bug Tracker": "https://github.com/gr4vy/gr4vy-python/issues",
    },
    python_requires=">=3.6",
    install_requires=[
        "certifi",
        "pycryptodome",
        "PyJWT",
        "pyOpenSSL",
        "DateTime",
        "setuptools",
        "six",
        "urllib3",
        "python-dateutil",
        "crypto",
        "cryptography", 
        "pem",
        "python-jose"],
    include_package_data=True)