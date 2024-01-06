# setup.py

from setuptools import setup, find_packages

setup(
    name='data_validation_library',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your library dependencies here
    ],
    python_requires='>=3.6',
    author='Prakhar Doneria',
    author_email='prakhardoneria3@gmail.com',
    description='A Python library for data validation and sanitization',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/prakhardoneria/data-validation-library',
    license='Apache-2.0 license',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
