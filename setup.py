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
    install_requires=["openapi-client==1.0.0",
	"pem==21.2.0",
	"PyJWT==2.3.0",
	"python-dateutil==2.8.2",
	"six==1.16.0",
	"urllib3==1.26.7"]
    )