from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ts2vec",
    version="0.1.0",
    description="A time series representation learning framework",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
) 