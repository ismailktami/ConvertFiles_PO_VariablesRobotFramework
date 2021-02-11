import os


class Convertor:
    @staticmethod
    def convertFilePoToRBF(file):
        file_rbf_str = "*** Variables ***\n\n"
        f = open(file, "r")
        lines = f.readlines()
        for line in lines:
            if str("msgid") in line:
                file_rbf_str = file_rbf_str + \
                    Convertor.extract_name_variable(line)
            if str("msgstr") in line:
                file_rbf_str = file_rbf_str + \
                    Convertor.extract_value_variable(line)
        if not os.path.exists("i18n_rbf"):
            os.makedirs('i18n_rbf')
        print(file_rbf_str)
        file_rbf = open("i18n_rbf/"+os.path.basename(f.name)+".txt", "w")
        file_rbf.write(file_rbf_str)
        file_rbf.close()
        file_rbf_str = '*** Variables ***\n\n'

    @staticmethod
    def extract_name_variable(line: str):
        if str('msgid ""') in line:
            return
        else:
            name_variable = '${'+line.strip('msgid').strip()+'}\t'
            return name_variable.replace('"', '')

    @staticmethod
    def extract_value_variable(line: str):
        if str('msgstr ""') in line:
            return
        else:
            value_variable = line.strip('msgstr').strip()
            return value_variable.replace('"', '')+'\n'
