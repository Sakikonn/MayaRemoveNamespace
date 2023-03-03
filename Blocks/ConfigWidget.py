# 这个是其中一个功能的Widget
from typing import Optional
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QDir
import PySide6.QtWidgets
import PySide6.QtCore

from WidgetComponents.Widget_Interface import Widget_Interface

import os
from Util.ConfigUtil import ConfigUtil
class ConfigWidget(QWidget, Widget_Interface):
    def __init__(this, *args) -> None:
        super().__init__(*args)
        ConfigUtil.LoadConfig()
        this.__confObj = ConfigUtil.GetConfigObj()
        pass

    def GetMayapyexe(this):
        return this.__confObj["mayapyexe"]


    # 选取mayapy.exe的路径 并保存
    def TBP_SelectMayaPyPathClicked(this):
        print("TBP_SelectMayaPyPathClicked")
        mayaPyRelativePath = "/bin/mayapy.exe"

        # 获取选择得mayapy目录
        directory = QFileDialog.getExistingDirectory(this, "Find Files",
                QDir.currentPath())
        mayapyexe = directory + mayaPyRelativePath
        if not os.path.isfile(mayapyexe):
            this.GetMainWindowUI().LET_DirMayaPy.setText(mayapyexe + "路径不存在")
            return
        this.GetMainWindowUI().LET_DirMayaPy.setText(mayapyexe)

        this.__confObj["mayapyexe"] = mayapyexe
        ConfigUtil.SaveConfig()
        print(mayapyexe)
    
    def ConfigChange(this,_Text):
        this.UpdateSaveButtonState(True)
        pass
    

    def SaveConfigEvent(this):
        _CharacterName = this.GetMainWindowUI().LE_CharacterName.text()
        _ModelName = this.GetMainWindowUI().LE_ModelName.text()
        _SkeletalName = this.GetMainWindowUI().LE_SkeletalName.text()

        this.__confObj["charactergroup"]["name"] = _CharacterName
        this.__confObj["charactergroup"]["skeletongroup"] = _SkeletalName
        this.__confObj["charactergroup"]["modelgroup"] = _ModelName

        ConfigUtil.SaveConfig()
        this.UpdateSaveButtonState(False)
        pass

    # UI
    def UpdateSaveButtonState(this,_Enable):
        this.GetMainWindowUI().PB_Config_Save.setEnabled(_Enable)

    def UpdateUIInfo(this):
        this.GetMainWindowUI().LET_DirMayaPy.setText(this.__confObj["mayapyexe"])
        this.GetMainWindowUI().LE_CharacterName.setText(this.__confObj["charactergroup"]["name"])
        this.GetMainWindowUI().LE_ModelName.setText(this.__confObj["charactergroup"]["modelgroup"])
        this.GetMainWindowUI().LE_SkeletalName.setText(this.__confObj["charactergroup"]["skeletongroup"])
        this.UpdateSaveButtonState(False)

