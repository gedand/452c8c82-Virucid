import glob
import os
import shutil
import sys

from werkzeug.utils import secure_filename

from flask import current_app as app
from helper.error_message import ErrorMessage
from helper.hex_to_img import caff_to_jpeg


def parsing(file):
    # TODO: implement
    # try:

        tmp_folder = "tmp_caff/"
        filename = secure_filename(file.filename)
        newfile = open(tmp_folder + filename, "w")
        newfile.close()
        file.save(tmp_folder + filename)
        file.close()

        path = os.getcwd()
        os.chdir(os.getcwd() + "\\tmp_caff")

        os.system("parser.exe " + filename)

        txt_files = glob.glob("*.txt")
        print(txt_files, len(txt_files))
        if len(txt_files) > 1:
            raise Exception('More than one .txts in /tmp_caff')

        jpeg_filename = caff_to_jpeg(txt_files[0])
        print(jpeg_filename)
        os.chdir(path)

        # fájlok átrakása
        source_path = 'tmp_caff/'
        dest_path = 'files/'
        d_caff_path = 'caff/'
        d_jpeg_path = 'img/'

        try:
            shutil.move(source_path + filename, dest_path + d_caff_path + filename)
        except Exception as e:
            app.logger.error(e)
        try:
            shutil.move(source_path + jpeg_filename, dest_path + d_jpeg_path + jpeg_filename)
        except Exception as e:
            app.logger.error(e)
        try:
            os.remove(source_path + txt_files[0])
        except Exception as e:
            app.logger.error(e)

        return filename, jpeg_filename

    # except Exception as e:
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    #     print(exc_type, fname, exc_tb.tb_lineno)
