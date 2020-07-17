import setuptools
from pathlib import Path

setuptools.setup(
    name='gym_npm',
    author='Anuj Pasricha',
    author_email='anuj.pasricha@colorado.edu',
    version='0.0.1',
    description='An OpenAI Gym Env for Nonprehensile Manipulation Tasks',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/a-nooj/gym-npm',
    packages=setuptools.find_packages(include='gym_npm*'),
    install_requires=['gym', 'pybullet', 'numpy', 'stable_baselines', 'tensorflow-gpu>=1.8.0,<2.0.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)
