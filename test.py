import os
from Convertor import Convertor


def extract_name_variable(line: str):
    if str('msgid ""') in line:
        return
    else:
        name_variable = '${'+line.strip('msgid').strip()+'}\t'
        return name_variable.replace('"', '')


def extract_value_variable(line: str):
    if str('msgstr ""') in line:
        return
    else:
        value_variable = line.strip('msgstr').strip()
        return value_variable.replace('"', '')+'\n'


for root, dirs, files in os.walk("i18n"):
    for file in files:
        if file.endswith("po"):
            file_rbf_str = "*** Variables ***\n\n"
            f = open(root+"/"+file, "r")
            lines = f.readlines()
            for line in lines:
                if str("msgid") in line:
                    file_rbf_str = file_rbf_str + extract_name_variable(line)
                if str("msgstr") in line:
                    file_rbf_str = file_rbf_str + extract_value_variable(line)
            if not os.path.exists(root+"/i18n_rbf"):
                os.makedirs(root+"/i18n_rbf")
            file_rbf = open(root+"/i18n_rbf/" +
                            os.path.basename(f.name)+".txt", "w")
            file_rbf.write(file_rbf_str)
            file_rbf.close()
            file_rbf_str = '*** Variables ***\n\n'
