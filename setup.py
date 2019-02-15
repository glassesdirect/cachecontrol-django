"""A cache provider for CacheControl using Django's caching mechanism."""

import setuptools

try:
    with open("README.markdown", "r") as fh:
        long_description = fh.read()  # pylint: disable=invalid-name
except IOError:
    # pylint: disable=invalid-name
    long_description = (
        "A cache provider for "
        "[CacheControl](https://cachecontrol.readthedocs.io/) "
        "using Django's caching mechanism."
    )

setuptools.setup(
    name="cachecontrol-django",
    version="0.0.0",
    author="MyOptique Group",
    author_email="tech@myoptiquegroup.com",
    description=__doc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glassesdirect/cachecontrol-django",
    packages=setuptools.find_packages(),
    install_requires=["cachecontrol", "django"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
