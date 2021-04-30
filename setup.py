import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snek-scripts",
    version="0.1.3c",
    author="",
    author_email="",
    description="A set of useful Python functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/supremestdoggo/Snek-Scripts",
    project_urls={
        "Bug Tracker": "https://github.com/supremestdoggo/Snek-Scripts/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)