import gzip
import shutil

from Modules.Log import LogUnzip, Logtime

def unzip_list(path, names, time):
    ''' Descomprime todos los .gz del dir '''
    for name in names:

        LogUnzip(time, name)

        dir_ = path+name

        with gzip.open(dir_, 'rb') as f_in:
            with open(dir_[:-3], 'wb') as f_out:
               shutil.copyfileobj(f_in, f_out)
    
    Logtime(time)
