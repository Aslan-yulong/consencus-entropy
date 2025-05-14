from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="consensus-entropy",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A library for calculating consensus entropy between multiple strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/consensus-entropy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "python-Levenshtein>=0.12.0",
    ],
) 