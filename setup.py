from setuptools import find_packages, setup

from move_dist import move_dist

version = "0.1.5"
name = "UniConvert"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=name,
    version=version,
    packages=find_packages(),
    install_requires=[
        "certifi==2023.11.17",
        "charset-normalizer==3.3.2",
        "colorama==0.4.6",
        "decorator==4.4.2",
        "docutils==0.20.1",
        "idna==3.6",
        "imageio==2.33.1",
        "imageio-ffmpeg==0.4.9",
        "importlib-metadata==7.0.1",
        "jaraco.classes==3.3.0",
        "keyring==24.3.0",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "more-itertools==10.1.0",
        "moviepy==1.0.3",
        "nh3==0.2.15",
        "numpy==1.26.2",
        "Pillow==10.1.0",
        "pkginfo==1.9.6",
        "proglog==0.1.10",
        "Pygments==2.17.2",
        "python-dotenv==1.0.0",
        "pywin32-ctypes==0.2.2",
        "readme-renderer==42.0",
        "requests==2.31.0",
        "requests-toolbelt==1.0.0",
        "rfc3986==2.0.0",
        "rich==13.7.0",
        "tqdm==4.66.1",
        "twine==4.0.2",
        "types-Pillow==10.1.0.2",
        "urllib3==2.1.0",
        "zipp==3.17.0",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)

move_dist(version)

"""
"certifi==2023.11.17"
"charset-normalizer==3.3.2"
"colorama==0.4.6"
"conversores_dudu==0.1"
"decorator==4.4.2"
"docutils==0.20.1"
"idna==3.6"
"imageio==2.33.1"
"imageio-ffmpeg==0.4.9"
"importlib-metadata==7.0.1"
"jaraco.classes==3.3.0"
"keyring==24.3.0"
"markdown-it-py==3.0.0"
"mdurl==0.1.2"
"more-itertools==10.1.0"
"moviepy==1.0.3"
"nh3==0.2.15"
"numpy==1.26.2"
"Pillow==10.1.0"
"pkginfo==1.9.6"
"proglog==0.1.10"
"Pygments==2.17.2"
"python-dotenv==1.0.0"
"pywin32-ctypes==0.2.2"
"readme-renderer==42.0"
"requests==2.31.0"
"requests-toolbelt==1.0.0"
"rfc3986==2.0.0"
"rich==13.7.0"
"tqdm==4.66.1"
"twine==4.0.2"
"types-Pillow==10.1.0.2"
"urllib3==2.1.0"
"zipp==3.17.0"
"""
