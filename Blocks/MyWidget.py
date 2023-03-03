# This Python file uses the following encoding: utf-8
# 这个是其中一个功能的Widget
from typing import Optional
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QDir
import PySide6.QtWidgets
import PySide6.QtCore
import subprocess
import time

from WidgetComponents.Widget_Interface import Widget_Interface
from Util.ResourceUtil import ResourceUtil
from Util.TempUtil import TempUtil
from Util.ConfigUtil import ConfigUtil
import Util.LogUtil as LogUtil
class MyWidget(QWidget, Widget_Interface):
    def __init__(this, *args) -> None:
        super().__init__(*args)
        this.CurPath = ""
        print("MyWidget Init...")

    def RunCmd(this,Command):
        print(Command)
        ret = subprocess.run(Command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="gbk")
        if ret.returncode == 0:
            print("success:",ret)
            print(ret.stdout)
        else:
            __logdir = TempUtil.GetLogPath()
            log_file = __logdir + "\\log_{}.txt".format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            with open(log_file,"w") as f:
                f.write("Output:{}\nError:\n{}".format(ret.stdout, ret.stderr))
                pass
        pass
    
    def PBT_StartClicked(this):
        import os
        print("PBT_StartClicked")
        __mayaexe = '"{}"'.format(this.GetMainWindowUI().ConfigWidget.GetMayapyexe())
        file_list = this.GetMainWindowUI().Files_Table.GetItemsFullPath()
        if len(file_list) == 0:
            return
        LogUtil.ClearLog()
        # this.GetMainWindowUI().ConfigWidget.ClearLog()
        for sourceFile in file_list:
            sourceFile = '/'.join(sourceFile.split("\\"))
            (fileDir,SaveFileName) = os.path.split(sourceFile)
            
            SaveFileDir = fileDir + "/newExport"
            if not os.path.isdir(SaveFileDir):
                os.mkdir(SaveFileDir)
            mayascript = '"{}"'.format(ResourceUtil.GetScript("RemoveNamespace3.py"))
            # DEBUG用的路径
            # mayascript = "./MayaScript/RemoveNamespace2.py"
            CharacterConfigObj = ConfigUtil.GetConfigObj()["charactergroup"]
            command = "{} {} {} {} {} {} {} {}".format(
                __mayaexe,mayascript,sourceFile,SaveFileDir,SaveFileName,CharacterConfigObj["name"],CharacterConfigObj["skeletongroup"],CharacterConfigObj["modelgroup"])
            this.RunCmd(command)
        QMessageBox.about(this,"Message","{}个模型处理完成...".format(len(file_list)))
        

    def TBT_SelectDirClicked(this):
        print("TBT_SelectDirClicked")
        directory = QFileDialog.getExistingDirectory(this, "Find Files",
                QDir.currentPath())
        this.GetMainWindowUI().LET_DirPath.setText(directory)
        
    def LET_DirPathTextChenge(this, _Path):
        if this.CurPath == _Path:
            return
        this.CurPath = _Path
        print(this.CurPath)
        this.GetMainWindowUI().Files_Table.find_files(this.CurPath)
    
    pass