import getpass
import os

class TempUtil():

    # 获取用户路径
    def GetUserFullPath():
        UserName = getpass.getuser()
        LocalPath = "C:\\Users\\{}\\AppData\\Local".format(UserName)
        return LocalPath

    def GetUtilTemp():
        return os.path.join(TempUtil.GetUserFullPath(),".KKUtilTemp")

    def GetLogPath():
        path = os.path.join(TempUtil.GetUtilTemp(),"Log")
        if not os.path.isdir(path):
            os.makedirs(path)
        return path

    def GetConfigPath():
        path = os.path.join(TempUtil.GetUtilTemp(),"Config")
        if not os.path.isdir(path):
            os.makedirs(path)
        return path