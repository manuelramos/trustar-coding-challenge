import setuptools

setuptools.setup(
    name="dot-notation-extractor-mr",
    version="0.0.1",
    author="Manuel Ramos",
    author_email="manuelramos175@gmail.com",
    description="A small example package to extract values of specific keys, expressed as dot-notation, from a json",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/manuelramos/trustar-coding-challenge",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)