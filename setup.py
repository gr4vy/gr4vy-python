import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gr4vy-python",
    version="0.0.1",
    packages=['gr4vy-python'],
    author="gr4vy",
    author_email="phillip@gr4vy.com",
    description="Gr4vy Python",
    url="https://github.com/gr4vy/gr4vy-python",
    project_urls={
        "Bug Tracker": "https://github.com/gr4vy/gr4vy-python/issues",
    },
    python_requires=">=3.6",
)