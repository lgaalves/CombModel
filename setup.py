from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='comb-model',
    version='1.0.0',
    license='MIT',
    author="Luiz G. A. Alves",
    author_email='lgaalves@northwestern.edu',
    description="A package to simulate Fractional Brownian walks on a comb-like structure.",
    long_description=long_description,
    long_description_content_type="text/x-rst; charset=UTF-8",
    packages=find_packages(),
    url='https://github.com/lgaalves/CombModel',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'stochastic','numpy','tqdm'
      ],

)