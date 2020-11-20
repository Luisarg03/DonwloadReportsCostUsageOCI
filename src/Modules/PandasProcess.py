#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import os
import glob
import json
import shutil

from Modules.Log import LogToJson, Logtime, LogRows

def PreProcess(path, subpath, folder_process, time):
    ''' Lee todos los .csv del directorio y los convierte a .json '''

    path_file = glob.glob(path+'*.csv')
    chunk = 1000000
    subfijo = 0
    count_row = 0

    for file_ in path_file:
        for chunks in pd.read_csv(file_, chunksize=chunk, low_memory=False):

            # ## Logeo
            LogToJson(time, file_[18:])

            id_ = file_[18:-4]
            count_row = count_row + chunks.shape[0]

            subfijo = subfijo + 1

            dic = chunks.to_dict(orient='records')
            
            # Crea el .json donde se guarda la data particionada
            jsonfile = open(subpath+id_+'_'+str(subfijo)+'.json', 'w')

            for row in dic:
                json.dump(row, jsonfile)
                jsonfile.write('\n')
        
            del chunks
            del dic

        os.remove(file_)

        # Move file
        shutil.move(file_+'.gz', folder_process+file_[18:]+'.gz')

        LogRows(time, file_[18:], count_row)

    # ## Fin de Logeo
    Logtime(time)