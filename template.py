# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 08:18:34 2023

@author: ElaheMsvi
"""

import os
from pathlib import Path
import logging


logging.basicConfig(level =logging.INFO ,format = '[%(ascitime)s]: %(message)s:')

project_name = 'text_summerizer'

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    
    ]    


for file_path in list_of_file:
    file_path = Path(file_path)
    file_dir , file_name = os.path.split(file_path)
    
    if file_dir!="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"creating directory: {file_dir} for {file_name}")
        
        
    if (not os.path.exists(file_path)) or (os.path.get_size(file_path)==0):
        with open(file_path,'w') as f:
            pass
            logging.info(f'creating empety file: {file_path}')
            
    else:
        logging.info(f'{file_name} already exists.')
        
            
            
            
        
        
        