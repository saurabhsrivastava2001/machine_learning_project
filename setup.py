#In Python, setup.py is a module used to build and distribute Python packages.
# It typically contains information about the package, such as its name, version, and dependencies,
# as well as instructions for building and installing the package. 
# This information is used by the pip tool, which is a package manager for 
# Python that allows users to install and manage Python packages from the command line. 
# By running the setup.py file with the pip tool,
# you can build and distribute your Python package so that others can use it.

from setuptools import find_packages,setup
from typing import List

hyfen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this funciton will return list of requirements
    '''
    requirements=[]
    
    #to remove the \n from every line 
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements =[req.replace("\n","") for req in requirements]

        #remove the  hyphen e . from the requirement.txt
        if hyfen_e_dot in requirements:
            requirements.remove(hyfen_e_dot)
            
    return requirements
setup(
    name="MLProject",
    verison='0.0.1',
    author='Saurabh',
    author_email='srisaurabh2001@gamil.com',
    packages=find_packages(),   
    install_requires=get_requirements('requirements.txt')
)

