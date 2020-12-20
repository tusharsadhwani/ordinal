import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ordinal",
    version="1.0.2",
    author="Tushar Sadhwani",
    author_email="tushar.sadhwani000@gmail.com",
    description="Get ordinals from numbers (42 -> 42nd).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tusharsadhwani/ordinal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pytest'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
