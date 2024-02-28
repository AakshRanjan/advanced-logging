from setuptools import setup, find_packages

# Read the contents of your README file.
with open('README.md', 'r') as file:
    long_description = f.read()

setup(
    name='advanced-logging',
    author='Aaksh Ranjan',
    version='0.0.1',
    package_dir={'': 'package'},
    packages=find_packages(),
    description='Advanced logging for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AakshRanjan/advanced-logging',
    license='MIT',
    classifiers=[
        'license :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    install_requires=["Flask >= 3.0.2"],
    python_requires='>=3.10',
)