from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "Translatify",
    version = "1.0.0",
    author = "Yateesh Reddy",
    author_email = "reddyyateesh999@gmail.com",
    description = "A translation tool for various languages.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/reddyyateesh/Translatify.git",
    # packages=["aiohttp", "requests"],
    packages = find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
