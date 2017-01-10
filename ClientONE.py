import os
import time


def wait_file_exit(filename, path):
    exit = False
    path = os.path.join(path, filename)
    millis1 = int(round(time.time() * 1000))
    while exit is False:
        if os.path.isfile(path):
            exit = True
    millis2 = int(round(time.time() * 1000))
    return(millis2 - millis1)


def sys_dir_path(*path):
    rootfolder = os.path.join(os.path.sep)
    for value in path:
        rootfolder = os.path.join(rootfolder, value)
    return rootfolder


def touch_file(filename, path):
    path = os.path.join(path, filename)
    command = 'touch %s' % (path)
    if os.path.isfile(path):
        print('success')
    os.system(command)


def main_client_ONE():
    filenameONE = 'touch1.file'
    filenameTWO = 'touch2.file'
    folderpath = sys_dir_path('home', 'cloud', '111_nfs')
    touch_file(filenameONE, folderpath)
    howlong = wait_file_exit(filenameTWO, folderpath)
    print(howlong)


if __name__ == '__main__':
    main_client_ONE()
