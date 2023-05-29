from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str):
    '''
    This function returns list of requirements...
    '''
    requirements=[]
    with open(file_path)as f:
        requirements=f.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
    



setup(
name='mlproject',
author="Komal Pandurang Shirkande",
author_email='komalshirkande123@gmail.com',
packages=find_packages(),
install_requires=['numpy','pandas','seaborn','matplotlib','scikit-learn']
)