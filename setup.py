from setuptools import setup, find_packages

setup(
    name='nlb_tools',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0,<=1.5.3',
        'scipy',
        'numpy',
        'scikit-learn',
        'h5py<4,>=2.9',
        'pynwb',
    ],
    author="Neural Latents",
)
