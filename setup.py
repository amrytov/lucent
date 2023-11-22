import lucent
from setuptools import setup, find_packages

version = lucent.__version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="torch-lucent-amr",
    packages=find_packages(exclude=[]),
    version=version,
    description=(
        "Lucid for PyTorch. "
        "Collection of infrastructure and tools for research in "
        "neural network interpretability."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Forked and messed up by AMR",
    author_email="amrytov@gmail.com",
    url="https://github.com/amrytov/lucent",
    license="Apache License 2.0",
    keywords=[
        "pytorch",
        "tensor",
        "machine learning",
        "neural networks",
        "convolutional neural networks",
        "feature visualization",
        "optimization",
    ],
    install_requires=[
        "torch>=2.1.0",
        "torchvision",
        "kornia",
        "tqdm",
        "numpy",
        "ipython",
        "pillow",
        "future",
        "decorator",
        "pytest",
        "pytest-mock",
        "coverage",
        "coveralls",
        "scikit-learn"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
