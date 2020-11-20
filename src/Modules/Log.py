import logging
import datetime

def LogDownload(time, name, size, time_file):
    logging.basicConfig(filename='../ControlDownload/'+time+'.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')

    logging.info('Descarga: '+ name +' // Peso: '+ str(round(size/1048576, 2))+' mb' +' // Fecha: '+ str(time_file))

def LogUnzip(time, name):
    logging.basicConfig(filename='../ControlDownload/'+time+'.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')

    logging.info('Descomprecion: '+name)


def LogToJson(time, name):
    logging.basicConfig(filename='../ControlDownload/'+time+'.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')

    logging.info('Conversion: '+name)


def LogRows(time, name, rows):
    logging.basicConfig(filename='../ControlDownload/'+time+'.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')

    logging.info('File: '+name+' // lineas: '+str(rows))


def LogAddLits(time, name):
    logging.basicConfig(filename='../ControlDownload/'+time+'.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')

    logging.info('Agregando a lista: '+name)


def Logtime(time):
    logging.basicConfig(filename='../ControlDownload/'+time+'.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')

    logging.info('--------------------------------------Finish--------------------------------------\n')


def LogFinish(time, period):
    logging.basicConfig(filename='../ControlDownload/'+time+'.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S')
                        
    end = datetime.datetime.now() - period
    logging.info('-------------------------Tiempo de proceso: '+ str(end) +'-------------------------')