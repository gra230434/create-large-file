import os
import sys

from classes.file_create import create_files

filecreate = create_files()
filecreate.CreateBegin(5, 'KB')
filecreate.InitCreate(run='off')
filecreate.CreateFile(number=15000)
