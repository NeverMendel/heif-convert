from setuptools import setup, find_packages

with open("heif_convert/_version.py", "r") as version_file:
    __version__ = version_file.read().split("=")[1].strip().strip('"')

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

setup(
    name="heif-convert",
    version=__version__,
    url="https://github.com/NeverMendel/heif-convert",
    license="MIT",
    author="Davide Cazzin",
    author_email="cazzindavide@gmail.com",
    description="Multi-Platform command line tool written in Python to convert HEIF images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["heif", "heic", "heif-convert", "heic-convert"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=["Pillow", "pillow-heif"],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "heif-convert=heif_convert.__main__:main",
        ]
    },
)
