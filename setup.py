# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:14:45 2022

@author: 6495
"""


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    install_reqs=[
        "numpy==1.18.1",
        "opencv_python==4.5.4.58",
        "torch==1.11.0",
        "openvino==2022.1.0",
    ],
    name="hse_mcv_dbface",
    version="0.0.3",
    author="polylam1994",
    author_email="polylam1994@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polylam1994/hse_mcv_MLinCV",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.6",
)
