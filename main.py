from classes.file_create import create_files

# 111_nfs
create1 = create_files('home', 'cloud', '111_nfs', '5KB')
create1.CreateBegin(5, 'KB')
create1.InitCreate(run='on')
create1.CreateFile(number=15000)
# 70_nfs
create2 = create_files('home', 'cloud', '70_nfs', '5KB')
create2.CreateBegin(5, 'KB')
create2.InitCreate(run='on')
create2.CreateFile(number=15000)
# 70_v001
create3 = create_files('home', 'cloud', '70_v001', '5KB')
create3.CreateBegin(5, 'KB')
create3.InitCreate(run='on')
create3.CreateFile(number=15000)
# samba_mount
create4 = create_files('home', 'cloud', 'samba_mount', '5KB')
create4.CreateBegin(5, 'KB')
create4.InitCreate(run='on')
create4.CreateFile(number=15000)
