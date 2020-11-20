#!/usr/bin/env python
# -*- coding: utf-8 -*-
import oci
import datetime
import os
import datetime

from Modules.ControlDownload import lastmod, filecontrol, cleardir
from Modules.Request import RequestDownload
from Modules.Unzip import unzip_list
from Modules.PandasProcess import PreProcess
from Modules.Log import LogFinish

folder_download = '../DownloadReport/'
folder_process = '../FilesProcess/'
json_folder = '../jsonReport/'
path = '../ControlDownload/'

reporting_namespace = 'bling'
prefix_file = "reports/cost-csv"
file_location = '../OciConfig/config.prod'

### Fechas para crear file de Logeo
now = datetime.datetime.now()
time = now.strftime("%Ya%mm%dd%Hh%Mm%Ss")

# ### Crea los dir si no existen ###
if not os.path.exists(folder_download):
    os.makedirs(folder_download)
    
if not os.path.exists(folder_process):
    os.makedirs(folder_process)

if not os.path.exists(json_folder):
    os.makedirs(json_folder)

if not os.path.exists(path):
    os.makedirs(path)


# ### configuracion de credenciales ###
config = oci.config.from_file(file_location=file_location)
reporting_bucket = config['tenancy']
object_storage = oci.object_storage.ObjectStorageClient(config)
fields = "name,size,timeCreated,timeModified"
report_bucket_objects = object_storage.list_objects(reporting_namespace,
                                                    reporting_bucket,
                                                    prefix=prefix_file,
                                                    fields=fields)


# ## Download Control
datetime_control = lastmod()
filecontrol = filecontrol()

# ## Descarga
data = RequestDownload(report_bucket_objects,
                       datetime_control,
                       filecontrol,
                       object_storage,
                       reporting_namespace,
                       reporting_bucket,
                       time,
                       folder_download)


# ## Agrega a la lista los nombres de los files descargados
file = open(path + '/' + 'FilesDownload.txt', 'a+')
for line in data:
    file.write(line + '\n')


# ## Descomprime los files nuevos
unzip_list(folder_download ,data, time)

# ## ToJson
PreProcess(folder_download, json_folder, folder_process, time)

LogFinish(time, now)
