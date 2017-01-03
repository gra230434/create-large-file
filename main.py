from classes.file_create import create_files

filesize = '5'
fileunit = 'MB'
filequantity = 1000

# 111_nfs
create1 = create_files('home', 'cloud', '111_nfs', filesize + fileunit)
create1.CreateBegin(filesize, fileunit)
create1.InitCreate(run='on')
create1.CreateFile(number=filequantity)
# 70_nfs
create2 = create_files('home', 'cloud', '70_nfs', filesize + fileunit)
create2.CreateBegin(filesize, fileunit)
create2.InitCreate(run='on')
create2.CreateFile(number=filequantity)
# 70_v001
create3 = create_files('home', 'cloud', '70_v001', filesize + fileunit)
create3.CreateBegin(filesize, fileunit)
create3.InitCreate(run='on')
create3.CreateFile(number=filequantity)
# samba_mount
create4 = create_files('home', 'cloud', 'samba_mount', filesize + fileunit)
create4.CreateBegin(filesize, fileunit)
create4.InitCreate(run='on')
create4.CreateFile(number=filequantity)
