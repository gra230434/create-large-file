from classes.file_create import create_files

filesize = '5'
fileunit = 'MB'
filequantity = 1000

# 111_nfs
create = create_files('', filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)

filesize = '2'
fileunit = 'MB'
filequantity = 10000

# 111_nfs
create = create_files('', filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateRandomFile(number=filequantity)

filesize = '5'
fileunit = 'MB'
filequantity = 25000

# 111_nfs
create = create_files('', filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)

filesize = '5'
fileunit = 'GB'
filequantity = 1

# 111_nfs
create = create_files('', filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)

filesize = '25'
fileunit = 'GB'
filequantity = 1

# 111_nfs
create = create_files('', filesize + fileunit)
create.CreateBegin(filesize, fileunit)
create.InitCreate(run='on')
create.CreateFile(number=filequantity)
