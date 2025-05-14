from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="consensus-entropy",
    version="0.1.0",
    author="Yulong Zhang",
    author_email="aslan.mingye@qq.com",
    description="A library for calculating consensus entropy between multiple strings, particularly useful for OCR result analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aslan.mingye@qq.com/consensus-entropy",
    project_urls={
        "Bug Tracker": "https://github.com/aslan.mingye@qq.com/consensus-entropy/issues",
        "Documentation": "https://github.com/aslan.mingye@qq.com/consensus-entropy#readme",
        "Source Code": "https://github.com/aslan.mingye@qq.com/consensus-entropy",
        "Paper": "https://arxiv.org/abs/2504.11101",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "python-Levenshtein>=0.12.0",
    ],
    keywords=[
        "ocr",
        "entropy",
        "consensus",
        "text-processing",
        "computer-vision",
        "machine-learning",
    ],
) 