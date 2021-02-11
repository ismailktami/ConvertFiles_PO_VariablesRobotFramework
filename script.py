file_rbf_str = '*** Variables ***\n\n'


def convertFilePoToRBF():
    f = open("fr.po", "r")
    lines = f.readlines()
    for line in lines:
        if str("msgid") in line:
            extract_name_variable(line)
        if str("msgstr") in line:
            extract_value_variable(line)
    file_rbf = open(f.name+".txt", "w")
    file_rbf.write(file_rbf_str)
    file_rbf.close()


def extract_name_variable(line: str):
    if str('msgid ""') in line:
        return
    else:
        name_variable = '${'+line.strip('msgid').strip()+'}\t'
        global file_rbf_str
        file_rbf_str = file_rbf_str + name_variable.replace('"', '')


def extract_value_variable(line: str):
    if str('msgstr ""') in line:
        return
    else:
        value_variable = line.strip('msgstr').strip()
        global file_rbf_str
        file_rbf_str = file_rbf_str + value_variable.replace('"', '')+'\n'


convertFilePoToRBF()
