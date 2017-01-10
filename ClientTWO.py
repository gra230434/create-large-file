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


def delete_file(path, *filename):
    for value in filename:
        filepath = os.path.join(path, value)
        if os.path.isfile(filepath):
            os.remove(filepath)


def wait_delete_file(path, *filename):
    for value in filename:
        exit = True
        filepath = os.path.join(path, value)
        while exit is True:
            if not os.path.isfile(filepath):
                exit = False


def main_client_TWO():
    filenameONE = 'touch1.file'
    filenameTWO = 'touch2.file'
    folderpath = sys_dir_path('nfs')
    delete_file(folderpath, filenameONE, filenameTWO)
    howlong = wait_file_exit(filenameONE, folderpath)
    touch_file(filenameTWO, folderpath)
    print(howlong)


if __name__ == '__main__':
    main_client_TWO()
