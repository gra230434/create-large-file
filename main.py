from classes.file_create import create_files

filesize = '5'
fileunit = 'MB'
filequantity = 1000

# 111_nfs
create1 = create_files('home', 'cloud', '111_nfs', filesize + fileunit)
create1.CreateBegin(filesize, fileunit)
create1.InitCreate(run='on')
create1.CreateFile(number=filequantity)
