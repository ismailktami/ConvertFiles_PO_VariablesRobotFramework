from Convertor import Convertor
import os
import sys
for file in os.listdir("i18n"):
    Convertor.convertFilePoToRBF("i18n/"+file)
