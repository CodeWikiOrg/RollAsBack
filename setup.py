
from setuptools import setup, find_packages

setup(
    name='rollasback',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    author_email='canrollas@codewiki.org',
    install_requires=[
        'requests',
        'urllib3'
    ],
    python_requires='>=3.6',
    description='Web backend framework written in Python named as RollAsBack.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',

)





