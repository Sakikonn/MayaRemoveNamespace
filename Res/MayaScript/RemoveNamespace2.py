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
# ����maya python ·��֮���ٵ���mayaģ��
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
        # �Ժ���ܸ�����������ֻ��һ��
        newclass = this.__class__
        # �ж���û�ж�ȡ��Json��û�оͶ�ȡ���룬�о�ֱ�ӷ���
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


# �ƶ��鵽��� ������һ���鲻����ʱ��ʧ�ܣ�
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
    mel.eval("FBXExportSmoothingGroups -v true")                    # ƽ����
    mel.eval("FBXExportHardEdges -v false")                         # 
    mel.eval("FBXExportTangents -v false")                          # ����
    mel.eval("FBXExportSmoothMesh -v true")                         # ƽ������
    mel.eval("FBXExportInstances -v false")                         # ����ʵ��
    mel.eval("FBXExportReferencedAssetsContent -v true")            # ���õ���Դ����
    mel.eval("FBXExportAnimationOnly -v false")                     # ������
    mel.eval("FBXExportBakeComplexAnimation -v false")              # ���ද��
    min_time = cmds.playbackOptions(q=True,ast=True)                # ��ȡ������ʼ֡
    max_time = cmds.playbackOptions(q=True,aet=True)                # ��ȡ��������֡
    mel.eval("FBXExportBakeComplexStart -v " + str(min_time))       # ��ʼ
    mel.eval("FBXExportBakeComplexEnd -v " + str(max_time))         # ����
    mel.eval("FBXExportBakeComplexStep -v 1")                       # ����
    mel.eval("FBXExportUseSceneName -v false")                      # ʹ�ó�������
    mel.eval("FBXExportQuaternion -v euler")                        # ��Ԫ����ֵģʽ
    mel.eval("FBXExportShapes -v true")                             # ����ģ��
    mel.eval("FBXExportSkins -v true")                              # ��Ƥ
    # Constraints
    mel.eval("FBXExportConstraints -v false")                       # Լ��
    mel.eval("FBXExportSkeletonDefinitions -v false")               # �Ǽܶ���
    # Cameras
    mel.eval("FBXExportCameras -v true")                            # ��Ӱ��
    # Lights
    mel.eval("FBXExportLights -v true")                             # �ƹ�
    # Embed Media
    mel.eval("FBXExportEmbeddedTextures -v false")                  # Ƕ���ý��
    # Connections
    mel.eval("FBXExportInputConnections -v true")                   # ����
    # Axis Conversion
    mel.eval("FBXExportUpAxis y")                                   # �Ϸ�����
    # Version
    mel.eval("FBXExportFileVersion -v FBX201600")                   # FBX �ļ���ʽ�汾
    mel.eval("FBXExportInAscii -v false")                           # FBX ����ΪASCII�ļ�

    # cmds.file(exportFileName, exportSelected=True, type="FBX export", force=True, prompt=False)
    cmds.file(exportFileName, force = True, options="v=0;", typ="FBX export", pr=True, es=True)
    # restore current user FBX settings
    setFBXSettings()


def StartScript(ExportFile):
    CharacterGroupName = GetCharacterGroup()
    # �Ƴ����ƿռ䡢�����½�ɫ����
    CharacterGroupName = RemoveNamespace(CharacterGroupName)
    print(CharacterGroupName)
    # ����ɫ���е�ģ����������� �ƶ�����ٶ���
    MoveGroupToOutLineAndExport(CharacterGroupName)
    exportFBX(ExportFile)

def OpenFbxFile():
    # ��fbx��mel����
    OpenFbxCommand = 'file -import -type "FBX"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "WangLing" -options "fbx"  -pr  -importFrameRate true  -importTimeRange "override" "{}";'.format(sourceFBXFile)
    mel.eval(OpenFbxCommand)
    StartScript(SaveFBXFullpath)
    pass




if __name__ == "__main__":
    # ��ʼ��Maya
    standalone.initialize(name = "python")
    cmds.loadPlugin("Mayatomr") # ��֪���Ǹ�ɶ
    cmds.loadPlugin("fbxmaya")
    OpenFbxFile()