# -*- coding: utf-8 -*-
import os
import zipfile
import random
from shutil import rmtree
from tqdm import tqdm
"""all files will be created in afilesdata folder"""


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
            createsize = size*1024
        elif self.unit == 'MB':
            createsize = size*1048576
        elif self.unit == 'GB':
            createsize = size*1073741824
        else:
            return 'FAIL'
        for value in tqdm(range(int(number))):
            filename = 'rand_%d.file' % (value)
            destfile = os.path.join(self.folder, filename)
            if not os.path.isfile(destfile):
                with open(destfile, 'wb') as fount:
                    fount.write(os.urandom(createsize))
        print('Create files success')
        return 'PASS'

    def CreateZIPBegin(self, zipfile='zipdata'):
        self.zipfile = os.path.join(self.rootfolder, zipfile)

    def RmZIPFile(self, run='on'):
        if run == 'on':
            if os.path.exists(self.zipfolder):
                rmtree(self.zipfolder)
            if not os.path.isdir(self.zipfolder):
                os.makedirs(self.zipfolder)
        return True

    def zipfiles(self):
        count = 1
        suffixname = '_0'
        filename = 'rand' + str(suffixname) + '.file'
        zippath = os.path.join(self.zipfolder, filename)
        while os.path.isfile(zippath):
            suffixname = '_' + str(count)
            filename = 'rand_' + str(suffixname) + '.file'
            zippath = os.path.join(self.zipfolder, filename)
            count += 1
        zf = zipfile.ZipFile(zippath, mode='w',
                             compression=zipfile.ZIP_DEFLATED, allowZip64=True)
        for root, folders, files in os.walk(self.initfolder):
            for sfile in files:
                aFile = os.path.join(root, sfile)
                zf.write(aFile)
        zf.close()
        return self.zipfolder
