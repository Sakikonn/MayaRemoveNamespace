import os,sys

class ResourceUtil():
    def Resource_path(relative_path=""):
        if getattr(sys, 'frozen' ,False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            base_path = os.path.abspath(os.path.join(base_path,"..\\"))

        return os.path.join(base_path,"Res",relative_path)

    def GetScript(RelativeScriptName):
        return os.path.join(ResourceUtil.Resource_path("MayaScript"),RelativeScriptName)