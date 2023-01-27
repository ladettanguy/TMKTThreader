from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
readme = (this_directory / "README.md").read_text()


setup(
    name='TMKTThreader',
    license='Apache 2.0',
    version='',
    author="Tanguy Ladet",
    maintainer="Tanguy Ladet",
    maintainer_email='sti2dlab.ladettanguy@gmail.com',
    author_email='sti2dlab.ladettanguy@gmail.com',
    packages=find_packages(include=['tmktthreader.*']),
    url='https://github.com/ladettanguy/TMKTThreader',
    download_url='https://github.com/ladettanguy/TMKTThreader.git',
    keywords=
    [
        'Thread',
        'Process',
        'Multi-process',
        "Multi-thread",
        "threading",
        "Async"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
    description="Easyfull multithreading package manager.",
    long_description=readme,
    long_description_content_type='text/markdown',
    zip_safe=False,
)
