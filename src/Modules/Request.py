# import oci
import datetime
from Modules.Log import LogDownload, Logtime

def RequestDownload(report_bucket_objects, datetime_control, filecontrol, object_storage, reporting_namespace, reporting_bucket, time, folder_download):
    ''' Download reports '''

    list_name = []

    for i in report_bucket_objects.data.objects:
        filename = i.name.rsplit('/', 1)[-1]

        time_file = i.time_created.strftime("%Y-%m-%d %H:%M:%S")
        time_file = datetime.datetime.strptime(time_file, '%Y-%m-%d %H:%M:%S')

        # # Control de duplicados
        if time_file > datetime_control and filename not in filecontrol:

            object_details = object_storage.get_object(reporting_namespace,
                                                       reporting_bucket,
                                                       i.name)

            # ## Logeo
            LogDownload(time, filename, i.size, time_file)

            with open(folder_download + filename, 'wb') as f:

                ### Descarga ###
                for chunk in object_details.data.raw.stream(2048 ** 2,
                                                            decode_content=False):
                    f.write(chunk)

            list_name.append(filename)
        
        else:
            pass
    
    file = open('../ControlDownload/UltimaHora.txt', 'w')
    file.write(str(time_file))

    # ## FinLogeoDownload
    Logtime(time)

    return list_name