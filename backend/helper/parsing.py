import glob
import os
import shutil
import string
import sys
from random import SystemRandom

from flask import current_app as app
from helper.hex_to_img import caff_to_jpeg
from werkzeug.utils import secure_filename


def parsing(file):
    try:

        tmp_folder = "tmp_caff/"
        filename = secure_filename(file.filename)
        newfile = open(tmp_folder + filename, "w")
        newfile.close()
        file.save(tmp_folder + filename)
        file.close()

        path = os.getcwd()
        os.chdir(path + "\\tmp_caff")

        os.system("parser.exe " + filename)

        txt_files = glob.glob("*.txt")  # TODO: uj parsernel majd .dat
        if len(txt_files) > 1:
            raise Exception('More than one .txts in /tmp_caff')

        jpeg_filename = caff_to_jpeg(txt_files[0])
        os.chdir(path)

        # fájlok átrakása
        source_path = 'tmp_caff/'
        dest_path = 'files/'
        d_caff_path = 'caff/'
        d_jpeg_path = 'img/'

        n_path = path + '/' + dest_path + d_caff_path[:-1]
        os.chdir(n_path)
        new_filename = None
        n = 16
        exists = True
        counter = 0
        while exists and counter < 1000:
            try:
                name = ''.join(SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(n))
                new_filename = name + '.caff'
                if new_filename not in os.listdir():
                    exists = False
            except:
                counter += 1
                pass

        if exists or new_filename is None:
            raise Exception('Can not find new name for uploaded files')

        os.chdir(path)

        try:
            shutil.move(source_path + filename, dest_path + d_caff_path + new_filename)
        except Exception as e:
            app.logger.error(e)
        new_filename = new_filename[:-4] + 'jpg'
        try:
            shutil.move(source_path + jpeg_filename, dest_path + d_jpeg_path + new_filename)
        except Exception as e:
            app.logger.error(e)
        try:
            os.remove(source_path + txt_files[0])
        except Exception as e:
            app.logger.error(e)

        return new_filename[:-4]

    except Exception as e:
        os.chdir(path)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, exc_obj, fname, exc_tb.tb_lineno)

        path = os.getcwd()
        os.chdir(path + "\\tmp_caff")
        files = os.listdir()

        for item in files:
            if not item.endswith("parser.exe"):
                os.remove(item)
        os.chdir(path)
        app.logger.error(e)
