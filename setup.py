# This file will be responsible for creating my ML
# application as a package, so that this package can be used/installed
# by me or anybody. e.g deploy this package inside pypy.

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        # this is to replace "\n", " " (space/blank)
        requirements = [req.replace("\n", " ") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Joydeep',
author_email = 'joycode17@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)
