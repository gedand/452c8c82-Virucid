import os

from werkzeug.utils import secure_filename


def parsing(file):
    # TODO: implement

    # print(type(file))
    # print(file.filename)
    # print(file.stream)
    # print(file.stream.read())
    tmp_folder = "tmp_caff/"

    newfile = open(tmp_folder + secure_filename(file.filename), "w")
    newfile.close()
    file.save(tmp_folder + secure_filename(file.filename))
    file.close()

    os.system("")

    return 'file'
