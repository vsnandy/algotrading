from setuptools import setup
from setuptools import find_namespace_packages

setup(
        name='algotrading',
        
        # Author info.
        author='Varun Nandyal',
        author_email='varun.nandyal@gmail.com',

        # Define Version info.
        version='0.0.1',

        # Description
        description='A Python app that allows users to perform various actions related to algorithmic trading.',

        # Repo location
        url='https://github.com/vsnandy/algotrading',

        # Define dependencies
        install_requires=[
            'requests',
            'pandas',
            'msal',
            'robin_stocks'
        ],

        # Specify folder content.
        packages=find_namespace_packages(
            include=['ms_graph']
        ),
        
        # Define the python version.
        python_requires='>3.7',
    )

