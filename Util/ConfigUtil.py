import json,os
from Util.TempUtil import TempUtil
# 加载配置信息
class ConfigUtil():
    __ConfigName = "KKConfigUtil.json"
    __ConfigPath = TempUtil.GetConfigPath()
    __FullConfigPath = os.path.join(__ConfigPath, __ConfigName)
    __ConfigObj = {}

    def GetConfigObj():
        return ConfigUtil.__ConfigObj
    def SetConfigObj(ConfObj):
        ConfigUtil.__ConfigObj = ConfObj

    def LoadConfig():
        print(ConfigUtil.__FullConfigPath)
        if not os.path.isfile(ConfigUtil.__FullConfigPath):
            ConfigUtil.CreateConfig()
        with open(ConfigUtil.__FullConfigPath) as f:
            ConfigUtil.__ConfigObj = json.load(f)
        pass

    def SaveConfig():
        with open(ConfigUtil.__FullConfigPath,'w') as f:
            json.dump(ConfigUtil.__ConfigObj, f)
        pass

    def CreateConfig():
        __config = {
                "charactergroup":{
                "name":"Group",
                "skeletongroup":"DeformationSystem",
                "modelgroup":"Geometry"
            },
            "mayapyexe":""
        }

        # 创建文件夹
        # os.makedirs(ConfigUtil.__ConfigPath)

        # 创建配置文件
        with open(ConfigUtil.__FullConfigPath,'w') as file_obj:
            json.dump(__config, file_obj)
        ConfigUtil.__ConfigObj = __config
        pass

import xml.etree.ElementTree as ET
class FBXExportSettings():
    def load_fbx_export_settings(file):
        tree = ET.ElementTree(file=file)
        root = tree.getroot()
        root.find


if __name__ == "__main__":
    

    pass