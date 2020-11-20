#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import os
import datetime


def cleardir(files):
    '''Limpia todos los comprimidos que no se hayan borrado
     antes de la descarga'''

    listfiles = glob.glob(files+'/*.gz')  # todo lo que existe
    for f in listfiles:
        os.remove(f)


def lastmod():
    '''Crea/lee el archivo que contiene la hora
     del ultimo archivo descargado'''

    path = '../ControlDownload'
    if not os.path.exists(path):
        os.makedirs(path)
        open(path + '/UltimaHora.txt', 'a+')
    else:
        pass

    try:
        file_time = open(path + '/' + 'UltimaHora.txt', 'r')
    except FileNotFoundError:
        file_time = open(path + '/' + 'UltimaHora.txt', 'a+')

    file_time = file_time.read()

    if file_time == '':
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")

        file_time = open(path + '/' + 'UltimaHora.txt', 'w')
        file_time.write(str(now)+'\n')

        file_time = open(path + '/' + 'UltimaHora.txt', 'r')
        file_time = file_time.read()
        file_time = file_time.strip()
        file_time = datetime.datetime.strptime(file_time, '%Y-%m-%d %H:%M:%S')
    else:
        file_time = open(path + '/' + 'UltimaHora.txt', 'r')
        file_time = file_time.read()
        file_time = file_time.strip()
        file_time = datetime.datetime.strptime(file_time, '%Y-%m-%d %H:%M:%S')

    return file_time


def filecontrol():
    '''Crea/Lee la lista de nombres de archivos que se descargaron'''

    path = '../ControlDownload'
    if not os.path.exists(path):
        os.makedirs(path)
        open(path + '/FilesDownload.txt', 'a+')
    else:
        pass

    try:
        file_name = open(path + '/' + 'FilesDownload.txt', 'r')
    except FileNotFoundError:
        file_name = open(path + '/' + 'FilesDownload.txt', 'a+')

    file_name = file_name.readlines()

    list_names = []

    for i in file_name:
        i = i.strip()
        list_names.append(i)

    return list_names
