from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
requirements = ["biopython>=1.79", "argparse>=1.4.0"]

setup(
    name='convertFQ',
    version='1.0',
    description='convertFQ is used to convert either DNA2RNA or RNA2DNA in a fastq file',
    url='https://github.com/NuruddinKhoiry/convertFQ.git',
    author='Ahmad Nuruddin Khoiri',
    author_email='nuruddinkhoiri34@gmail.com',
    license='unlicense',
    packages=['convertFQ'],
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    zip_safe=False
)