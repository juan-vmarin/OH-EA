import setuptools

with open("README.md", "r",encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="group10",
    version="1.0.0",
    author="Group10",
    author_email="author@example.com",
    description="Heuristic optimization 1st practical work, by Group 10.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
