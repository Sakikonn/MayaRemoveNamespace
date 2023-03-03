# This Python file uses the following encoding: utf-8

import os,json
import sys
try:
    sourceFBXFile = sys.argv[1]
    saveFileDir = sys.argv[2]
    saveFileName = sys.argv[3]
    print(sourceFBXFile,saveFileDir,saveFileName)
    if not os.path.isfile(sourceFBXFile):
        raise Exception(saveFileDir,"source FBX is not..")

    if not os.path.isdir(saveFileDir):
        raise Exception(saveFileDir,"export FBX dir is not..")

except Exception as e:
    if isinstance(e, IndexError):
        print("Parameter is missing .... <sourceFBXFile> <FileDir> <FileName>")
    else:
        print(str(e))
    sys.exit()

SaveFBXFullpath = os.path.normpath( os.path.join(saveFileDir,saveFileName) )
print(SaveFBXFullpath)
# 导入maya python 路径之后再导入maya模块
from maya import cmds,mel,standalone


class MyConfig():
    __CharacterStruct = """{
    "CharacterGroup":"Group",
    "skeletonGroup":"DeformationSystem",
    "modelGroup":"Geometry"
    }"""

    __ObjectStrutc = None

    def __init__(this):
        pass

    def GetJsonObject(this):
        # 以后可能改类名、方便只改一次
        newclass = this.__class__
        # 判断有没有读取过Json、没有就读取存入，有就直接返回
        if newclass.__ObjectStrutc == None:
            newclass.__ObjectStrutc = json.loads(newclass.__CharacterStruct)

        return newclass.__ObjectStrutc

    # skeletonGroup
    def GetSkeletonGroup(this):
        return this.GetJsonObject()['skeletonGroup']
    # modelGroup
    def GetModelGroup(this):
        return this.GetJsonObject()['modelGroup']
    # CharacterGroup
    def GetCharacterGroup(this):
        return this.GetJsonObject()['CharacterGroup']

    pass


def GetCharacterGroup():
    CharacterGroupName = MyConfig().GetCharacterGroup()
    TopObjs = cmds.ls(assemblies=True)
    for obj in TopObjs:
        if obj.split(":")[-1] == CharacterGroupName:
            return obj
    return None
    
def RemoveNamespace(GroupName,IncludeYourself = True):
    GroupAllobj = cmds.listRelatives(GroupName, ad = True)
    if GroupAllobj == None:
        return
    if IncludeYourself:
        GroupName = cmds.rename(GroupName, GroupName.split(":")[-1])

    for obj in GroupAllobj:
        cmds.rename(obj, obj.split(":")[-1])

    return GroupName
    pass


# 移动组到大纲 （其中一个组不存在时即失败）
def MoveGroupToOutLineAndExport(GroupName):
    SkeletonGroupName = MyConfig().GetSkeletonGroup()
    ModelGroupName = MyConfig().GetModelGroup()

    CharacterChilds = cmds.listRelatives(GroupName)
    if SkeletonGroupName in CharacterChilds and ModelGroupName in CharacterChilds:
        cmds.parent(ModelGroupName, w=True)
        cmds.parent(SkeletonGroupName, w=True)
        
        cmds.select((ModelGroupName,SkeletonGroupName))

def exportFBX(exportFileName): # , min_time, max_time
    def getFBXSettings():
        # get current user settings for FBX export and store them
        mel.eval('FBXPushSettings;')


    def setFBXSettings():
        # set user-defined FBX settings back after export
        mel.eval('FBXPopSettings;')

    # store current user FBX settings
    getFBXSettings()

    # export selected as FBX
    # Geometry
    mel.eval("FBXExportSmoothingGroups -v true")                    # 平滑组
    mel.eval("FBXExportHardEdges -v false")                         # 
    mel.eval("FBXExportTangents -v false")                          # 切线
    mel.eval("FBXExportSmoothMesh -v true")                         # 平滑网格
    mel.eval("FBXExportInstances -v false")                         # 保留实例
    mel.eval("FBXExportReferencedAssetsContent -v true")            # 引用的资源内容
    mel.eval("FBXExportAnimationOnly -v false")                     # 仅动画
    mel.eval("FBXExportBakeComplexAnimation -v false")              # 烘培动画
    min_time = cmds.playbackOptions(q=True,ast=True)                # 获取动画开始帧
    max_time = cmds.playbackOptions(q=True,aet=True)                # 获取动画结束帧
    mel.eval("FBXExportBakeComplexStart -v " + str(min_time))       # 开始
    mel.eval("FBXExportBakeComplexEnd -v " + str(max_time))         # 结束
    mel.eval("FBXExportBakeComplexStep -v 1")                       # 步长
    mel.eval("FBXExportUseSceneName -v false")                      # 使用场景命名
    mel.eval("FBXExportQuaternion -v euler")                        # 四元数插值模式
    mel.eval("FBXExportShapes -v true")                             # 变形模型
    mel.eval("FBXExportSkins -v true")                              # 蒙皮
    # Constraints
    mel.eval("FBXExportConstraints -v false")                       # 约束
    mel.eval("FBXExportSkeletonDefinitions -v false")               # 骨架定义
    # Cameras
    mel.eval("FBXExportCameras -v true")                            # 摄影机
    # Lights
    mel.eval("FBXExportLights -v true")                             # 灯光
    # Embed Media
    mel.eval("FBXExportEmbeddedTextures -v false")                  # 嵌入的媒体
    # Connections
    mel.eval("FBXExportInputConnections -v true")                   # 连接
    # Axis Conversion
    mel.eval("FBXExportUpAxis y")                                   # 上方向轴
    # Version
    mel.eval("FBXExportFileVersion -v FBX201600")                   # FBX 文件格式版本
    mel.eval("FBXExportInAscii -v false")                           # FBX 导出为ASCII文件

    # cmds.file(exportFileName, exportSelected=True, type="FBX export", force=True, prompt=False)
    cmds.file(exportFileName, force = True, options="v=0;", typ="FBX export", pr=True, es=True)
    # restore current user FBX settings
    setFBXSettings()


def StartScript(ExportFile):
    CharacterGroupName = GetCharacterGroup()
    # 移除名称空间、并更新角色组名
    CharacterGroupName = RemoveNamespace(CharacterGroupName)
    print(CharacterGroupName)
    # 将角色组中的模型组与骨骼组 移动到大纲顶层
    MoveGroupToOutLineAndExport(CharacterGroupName)
    exportFBX(ExportFile)

def OpenFbxFile():
    # 打开fbx的mel命令
    OpenFbxCommand = 'file -import -type "FBX"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "WangLing" -options "fbx"  -pr  -importFrameRate true  -importTimeRange "override" "{}";'.format(sourceFBXFile)
    mel.eval(OpenFbxCommand)
    StartScript(SaveFBXFullpath)
    pass




if __name__ == "__main__":
    # 初始化Maya
    standalone.initialize(name = "python")
    cmds.loadPlugin("Mayatomr") # 不知道是个啥
    cmds.loadPlugin("fbxmaya")
    OpenFbxFile()