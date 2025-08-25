from setuptools import setup,find_packages

setup(
    name='cycon',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires = ['Click'],
    entry_points='''
        [console_scripts]
        cycon=src.commands.commands:cycon
    '''
)