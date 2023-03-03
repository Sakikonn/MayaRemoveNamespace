from Util.TempUtil import TempUtil
# from TempUtil import TempUtil
import os
def ClearLog():
    path = TempUtil.GetLogPath()
    ls = os.listdir(path)
    for i in ls:
        filepath = os.path.join(path,i)
        if os.path.isfile(filepath):
            os.remove(filepath)
        print(i)