# from PySide6.QtWidgets import (QApplication, QSizePolicy, QToolBox, QVBoxLayout,
#     QWidget)
# from Widgets.FBXExportSettings.ui_FBXExportSettings import Ui_FBXExportSettings

# class FBXExportSettings(QWidget):
#     def __init__(self, *args) -> None:
#         super().__init__(*args)
#         self.ui = Ui_FBXExportSettings()
#         self.ui.setupUi(self)

#     def My__init__(self):
#         pass

import xml.etree.ElementTree as ET
class FBXExportSettingsConfig(object):
    def LoadConfig(self,file):
        tree = ET.ElementTree(file=file)
        root = tree.getroot()
        IncludeGrp = root.find("IncludeGrp")
        AdvOptGrp = root.find("AdvOptGrp")

        FBXExportSettings = {}

        for i in IncludeGrp.iter():
            if len(i) == 0:
                try:
                    FBXExportSettings[i.tag] = i.attrib["v"]
                except Exception as e:
                    print(e)
        
        for i in AdvOptGrp.iter():
            if len(i) == 0:
                try:
                    FBXExportSettings[i.tag] = i.attrib["v"]
                except Exception as e:
                    print(e)
        print(FBXExportSettings)

    pass

if __name__ == "__main__":
    FBXExportSettingsConfig().LoadConfig("E:/Work/MayaBatchToUE5Tool/MayaPython/NameSpaceRemove/Res/FbxExportSettings/FBXExport.fbxexportpreset.xml")

    pass
