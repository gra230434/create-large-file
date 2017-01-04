# -*- coding: utf-8 -*-
import os
import random
import multiprocessing
from shutil import rmtree
from tqdm import tqdm
"""all files will be created in afilesdata folder"""


def writetofile(filename, inputsize):
    bigfile = open(filename, 'wb')
    bigfile.write(os.urandom(inputsize))
    bigfile.close()


class create_files:

    def __init__(self, *path):
        """ init class """
        self.rootfolder = os.path.join(os.path.sep)
        for value in path:
            self.rootfolder = os.path.join(self.rootfolder, value)
        print self.rootfolder
        if not os.path.isdir(self.rootfolder):
            os.makedirs(self.rootfolder)

    def CreateBegin(self, filesize, unit, folder=''):
        self.filesize = filesize
        unit = unit.upper()
        if unit == 'KB' or unit == 'MB' or unit == 'GB':
            self.unit = unit
        else:
            self.unit = 'KB'
        if folder:
            self.folder = self.rootfolder
        else:
            self.folder = os.path.join(self.rootfolder, folder)

    def InitCreate(self, run='on'):
        if run == 'on':
            if os.path.exists(self.folder):
                rmtree(self.folder)
            if not os.path.isdir(self.folder):
                os.makedirs(self.folder)
        elif run == 'off':
            if not os.path.isdir(self.folder):
                os.makedirs(self.folder)
        return 'PASS'

    def CreateFile(self, number=1):
        size = int(self.filesize)
        if self.unit == 'KB':
            create = 1024
        elif self.unit == 'MB':
            create = 1048576
        elif self.unit == 'GB':
            create = 1073741824
        else:
            return 'FAIL'
        for value in tqdm(range(int(number))):
            filename = 'rand_%d.file' % (value)
            destfile = os.path.join(self.folder, filename)
            for i in range(size):
                the_proc = multiprocessing.Process(target=writetofile,
                                                   args=((destfile), (create)))
                the_proc.start()
                the_proc.join()
        print('Create files success')
        return 'PASS'

    def CreateRandomFile(self, number=1):
        size = round(random.uniform(0.5, 3.1), 2) * 10
        create = 1024*103
        for value in tqdm(range(int(number))):
            filename = 'rand_%d.file' % (value)
            destfile = os.path.join(self.folder, filename)
            for i in range(int(size)):
                the_proc = multiprocessing.Process(target=writetofile,
                                                   args=((destfile), (create)))
                the_proc.start()
                the_proc.join()
        print('Create files success')
        return 'PASS'
