import os
import sys
from script import Convertor
for file in os.listdir("i18n"):
    Convertor.convertFilePoToRBF("i18n/"+file)
