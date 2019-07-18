from setuptools import setup
from setuptools import find_packages

long_description = """
To AI builds on top of Tensorflow and provides utility and
helper functions for the most common deep learning tasks.
"""

setup(
    name="To AI",
    version="0.0.1",
    description="To AI helper library",
    long_description=long_description,
    author="Dovydas Ceilutka",
    author_email="dovydas.ceilutka@gmail.com",
    url="https://github.com/mokahaiku/toai",
    download_url="https://github.com/mokahaiku/toai",
    license="MIT",
    install_requires=[
        "tensorflow>=2.0.0-beta1",
        "attrs",
        "imagehash",
        "funcy",
        "Pillow",
        "seaborn",
        "numpy",
        "pandas",
        "sklearn",
        "fastprogress",
    ],
    extras_require={
        "tests": [
            "pytest",
            "pytest-pep8",
            "pytest-xdist",
            "pytest-cov",
            "pytest-timeout",
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
)
