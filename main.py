from classes.file_create import create_files

filesize = '5'
fileunit = 'MB'
folder = ''
filequantity = 1000

create = create_files(folder, filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)

filesize = '2'
fileunit = 'MB'
filequantity = 1000

create = create_files(folder, filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateRandomFile(number=filequantity)

filesize = '5'
fileunit = 'MB'
filequantity = 2000

create = create_files(folder, filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)

filesize = '5'
fileunit = 'GB'
filequantity = 1

create = create_files(folder, filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)

filesize = '10'
fileunit = 'GB'
filequantity = 1

create = create_files(folder, filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)
