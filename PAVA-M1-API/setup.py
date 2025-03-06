from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="PAVA-0.0.1",
    version="0.1",
    author="indranil Bakshi",
    author_email="officialindranilbakshi@gmail.com",
    description="Pre trained Virtual Assistance",

    packages=find_packages(),

    install_requires=requirements,
    python_requires=">=3.7"
)